import pandas as pd
import os

# Define directory for saving item details CSVs
links_folder = 'scraper/links/'
items_folder = 'scraper/items/'
output_file = 'data/women-top-rated.csv'
materials_file = 'data/materials.csv'

# Get the most recent list of links
def get_most_recent_csv(directory):
    csv_files = [f for f in os.listdir(directory) if f.endswith('.csv')]
    csv_files.sort(reverse=True)
    return os.path.join(directory, csv_files[0]) if csv_files else None

links_file = get_most_recent_csv(links_folder)
links = pd.read_csv(links_file) if links_file else []

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
    existing_materials = set(existing_materials_df['Material'])
else:
    existing_materials = set()

# Filter new materials that are not in existing_materials
new_materials = new_material_set - existing_materials

# Proceed only if there are new materials to add
if new_materials:
    new_materials_df = pd.DataFrame(list(new_materials), columns=['Material'])
    new_materials_df['Biodegradable'] = ''
    new_materials_df['Natural'] = ''
    new_materials_df['Attributes'] = ''

    # Append new materials to the existing DataFrame (if it exists) or create a new one
    if 'existing_materials_df' in locals():
        updated_materials_df = pd.concat([existing_materials_df, new_materials_df], ignore_index=True)
    else:
        updated_materials_df = new_materials_df

    # Save the updated DataFrame to materials.csv
    updated_materials_df.to_csv(materials_file, index=False)

# Iterate through each material in updated_materials_df
for material in updated_materials_df['Material']:
    # Add a new column for each material in consolidated_df and set default value to 0
    consolidated_df[material] = 0

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
    # Extract and round material percentages
    composition = row['Composition']
    material_percentages = extract_material_percentages(composition)

    # Update the material columns with their respective rounded percentages
    for material, percentage in material_percentages.items():
        if material in consolidated_df.columns:
            consolidated_df.at[index, material] = percentage

# Add a 'Type' column to consolidated_df
consolidated_df['Type'] = consolidated_df['Title'].apply(lambda title: title.split()[-1] if isinstance(title, str) else '')    

# Count the frequency of each unique value in the 'Type' column
type_counts = consolidated_df['Type'].value_counts()
print(type_counts)

# Save consolidated df as CSV
consolidated_df.to_csv(output_file, index=False)
