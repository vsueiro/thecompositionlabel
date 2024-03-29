import pandas as pd
import os
import re
import datetime

# Define directory for saving item details CSVs
links_folder = 'scraper/links/'
items_folder = 'scraper/items/'
output_file = 'public/data/items.csv'
materials_file = 'public/data/materials.csv'
meta_file = 'public/data/meta.csv'
weird_items_file = 'public/data/weird-items.csv'

def get_recent_csv_files(directory, num_files=14):
    csv_files = [f for f in os.listdir(directory) if f.endswith('.csv')]
    csv_files.sort(reverse=True)
    return [os.path.join(directory, csv_files[i]) for i in range(min(len(csv_files), num_files))]

def combine_csv_files(file_paths):
    dfs = []
    for file_path in file_paths:
        df = pd.read_csv(file_path)
        dfs.append(df)
    return pd.concat(dfs, ignore_index=True)

def preprocess_dataframe(df):
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])  # Ensure Timestamp is in datetime format
    df.sort_values(by=['Item ID', 'Timestamp'], ascending=[True, False], inplace=True)
    df.drop_duplicates(subset='Item ID', keep='first', inplace=True)
    return df

# Assuming `links_folder` is defined and points to the directory with your CSV files
recent_links_files = get_recent_csv_files(links_folder)
combined_links_df = combine_csv_files(recent_links_files)
links = preprocess_dataframe(combined_links_df)

# `links` is now the DataFrame with combined data from the most recent 14 CSV files,
# with duplicates removed based on `Item ID`, keeping the entry with the most recent `Timestamp`.

# Initialize an empty DataFrame for the consolidated data
consolidated_df = pd.DataFrame()

# Iterate over each row in the links DataFrame
for _, row in links.iterrows():
    item_id = row['Item ID']
    file_path = f'{items_folder}{item_id}.csv'

    # Check if the file exists
    if os.path.exists(file_path):
        # Read the CSV file
        item_df = pd.read_csv(file_path)

        # Get Type from older link standard
        if 'Type' not in item_df.columns:

            # Regular Expression to extract numbers between '-cat-' and '.html'
            pattern = r'-cat-(\d+)\.html'

            # Extract the desired substring using regex
            link_value = item_df.loc[0, 'Link']
            match = re.search(pattern, link_value)

            # Check if there is a match and extract the value
            extracted_value = match.group(1) if match else ""

            # Assign the extracted value to the 'Type' column of the first row
            item_df.at[0, 'Type'] = extracted_value

        # Append this DataFrame to the consolidated DataFrame
        consolidated_df = pd.concat([consolidated_df, item_df], ignore_index=True)

# Extract unique materials from the 'Composition' column
new_material_set = set()
for composition in consolidated_df['Composition'].dropna():
    materials = composition.split(',')
    for material in materials:
        material_name = material.split('%')[-1].strip()  # Remove percentage and strip spaces
        new_material_set.add(material_name)

# Check if materials.csv exists and read it
if os.path.exists(materials_file):
    existing_materials_df = pd.read_csv(materials_file)
    existing_materials = set(existing_materials_df['Name'])
else:
    existing_materials = set()

# Filter new materials that are not in existing_materials
new_materials = new_material_set - existing_materials

# Initialization outside the if block
updated_materials_df = pd.DataFrame() 

# Proceed only if there are new materials to add
if new_materials:
    new_materials_df = pd.DataFrame(list(new_materials), columns=['Name'])
    new_materials_df['Biodegradable'] = False
    new_materials_df['Natural'] = ''
    new_materials_df['Attributes'] = ''
    new_materials_df['Checked'] = False

    # Append new materials to the existing DataFrame (if it exists) or create a new one
    if 'existing_materials_df' in locals():
        updated_materials_df = pd.concat([existing_materials_df, new_materials_df], ignore_index=True)
    else:
        updated_materials_df = new_materials_df

    # Save the updated DataFrame to materials.csv
    updated_materials_df.to_csv(materials_file, index=False)

# Only iterate if 'updated_materials_df' is not empty
if not updated_materials_df.empty:
    for material in updated_materials_df['Name']:
        # Add a new column for each material in consolidated_df and set default value to 0
        consolidated_df[material] = 0

def clean_composition(composition):
    try:
        # Split the string by commas and strip whitespace
        materials = [mat.strip() for mat in composition.split(',')]
    except AttributeError:
        # Print the problematic composition and re-raise the error
        print(f"Error with composition: {composition}")
        raise
    
    # Remove duplicates while preserving order
    seen = set()
    unique_materials = [x for x in materials if not (x in seen or seen.add(x))]

    # Join the unique materials back into a string
    return ', '.join(unique_materials)


# Function to extract and round material percentages from composition string
def extract_material_percentages(composition):
    # Split the composition by comma and extract material and percentage
    materials = composition.split(',')
    percentages = {}
    for material in materials:
        parts = material.split('%')
        if len(parts) == 2:
            percentage, material_name = parts
            try:
                # Convert the percentage to float, round it, and handle any ValueError
                percentages[material_name.strip()] = round(float(percentage.strip()))
            except ValueError:
                # Handle cases where the percentage part is not a valid number
                print(f"Warning: Invalid percentage value '{percentage}' in composition '{composition}'")
    return percentages

# Iterate through each row in consolidated_df
for index, row in consolidated_df.iterrows():

    # Clean the composition string and update the 'Composition' column
    composition = clean_composition(row['Composition'])
    consolidated_df.at[index, 'Composition'] = composition

    # Extract and round material percentages from the cleaned composition
    material_percentages = extract_material_percentages(composition)

    # Update the material columns with their respective rounded percentages
    for material, percentage in material_percentages.items():
        if material not in consolidated_df.columns:
            consolidated_df[material] = 0  # Initialize a new column with 0
        consolidated_df.at[index, material] = percentage

# Drop duplicate rows from the DataFrame
consolidated_df = consolidated_df.drop_duplicates()

# Update count of items that contain each material
if os.path.exists(materials_file):
    existing_materials_df = pd.read_csv(materials_file)

    # Ensure Count column exists and set all its values to 0
    existing_materials_df['Count'] = 0

    # Create a new column for Median and set it to 0
    existing_materials_df['Median'] = 0

    # Update Count column
    for name in existing_materials_df['Name']:
        if name in consolidated_df.columns:
            # Counting items with material usage > 0
            count = (consolidated_df[name] > 0).sum()
            existing_materials_df.loc[existing_materials_df['Name'] == name, 'Count'] = count

            # Calculating median of non-zero material usage
            median = consolidated_df[consolidated_df[name] > 0][name].median()
            existing_materials_df.loc[existing_materials_df['Name'] == name, 'Median'] = median

    # Calculate the total of the 'Count' column
    total_count = existing_materials_df['Count'].sum()

    # Create the 'Percent' column
    existing_materials_df['Percent'] = (existing_materials_df['Count'] / total_count) * 100

    # Save the updated DataFrame to materials.csv
    existing_materials_df.to_csv(materials_file, index=False)

    # Check if items are fully biodegradable

    # Initialize 'Biodegradable' column with False
    consolidated_df['Biodegradable'] = False

    # Initialize 'BiodegradableRatio' column with 0
    consolidated_df['BiodegradableRatio'] = 0

    # Initialize 'MaterialCount' column with 0
    consolidated_df['MaterialCount'] = 0

    # Convert materials_df to dictionary for faster lookup
    biodegradable_dict = dict(zip(existing_materials_df['Name'], existing_materials_df['Biodegradable']))

    # Iterate over each row in the DataFrame
    for index, row in consolidated_df.iterrows():

        # Check each item's materials and update 'Biodegradable' if applicable
        is_biodegradable = True
        for material in biodegradable_dict:
            if material in consolidated_df.columns and row[material] > 0 and not biodegradable_dict[material]:
                is_biodegradable = False
                break
        consolidated_df.at[index, 'Biodegradable'] = is_biodegradable

        # For each biodegradable material
        for material, is_biodegradable in biodegradable_dict.items():
            if is_biodegradable:
                # Check if the material is in the row and add its percentage
                if material in consolidated_df.columns:
                    consolidated_df.at[index, 'BiodegradableRatio'] += row[material]

        # Count how many materials this item contains
        count = 0
        for material in biodegradable_dict.keys():
            if material in consolidated_df.columns and row[material] > 0:
                count += 1
        consolidated_df.at[index, 'MaterialCount'] = count

    # Ensure that BiodegradableRatio does not exceed 100
    consolidated_df['BiodegradableRatio'] = consolidated_df['BiodegradableRatio'].clip(upper=100)

# Check for weird items (e.g., duplicated materials in composition)
        
def check_duplicated_materials(text):
    # Regular expression to find patterns like '95% ' or '50.0% ' and remove them
    clean_string = re.sub(r'\d+(\.\d+)?%\s*', '', text)
    
    # Remove commas
    clean_string = clean_string.replace(',', '')
    
    words = clean_string.split()
    seen = set()
    for word in words:
        if word in seen:
            return True
        seen.add(word)
    return False

# Filter the DataFrame directly using the check_duplicated_materials function
weird_items = consolidated_df[consolidated_df['Composition'].apply(check_duplicated_materials)]

# Save to CSV
weird_items.to_csv(weird_items_file, index=False)

# Save the DataFrame without duplicates as a CSV file
consolidated_df.to_csv(output_file, index=False)

# Writing metadata to a file

# Calculate summary values
total_items = len(consolidated_df)
biodegradable_count = consolidated_df[consolidated_df['Biodegradable'] == True].shape[0]
ratio = (biodegradable_count / total_items) * 100

# Extracting just the file name (without .csv)
file_name = recent_links_files[0].split('/')[-1].replace('.csv', '')

# Formatting the date and time as an ISO date
date_time_str = file_name.replace('-', '')
iso_date_time = datetime.datetime.strptime(date_time_str, '%Y%m%d%H%M%S').isoformat()

# Creating a new DataFrame with the required data
data = {'Updated': [iso_date_time], 'Items': [total_items], 'Biodegradable': [biodegradable_count], 'Ratio': [ratio]}
summary_df = pd.DataFrame(data)

# Save the new DataFrame to a CSV file
summary_df.to_csv(meta_file, index=False)