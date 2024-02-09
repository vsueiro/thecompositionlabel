from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import datetime
import random
import re
import os
import time
import json

# Define directory for saving item details CSVs
output_folder = 'scraper/items/'
links_folder = 'scraper/links/'

# Define the amount of links per scraping batch
limit = 200

# Get the most recent list of links
def get_most_recent_csv(directory):
    csv_files = [f for f in os.listdir(directory) if f.endswith('.csv')]
    csv_files.sort(reverse=True)
    return os.path.join(directory, csv_files[0]) if csv_files else None

links_file = get_most_recent_csv(links_folder)
links = pd.read_csv(links_file) if links_file else []

# Shuffle links order
randomized_links = links.sample(frac=1).reset_index(drop=True)

# Prioritize links order
existing_links = []
new_links = []

for _, row in randomized_links.iterrows():
    item_id = row['Item ID']
    link = row['Link']
    file_path = f'{output_folder}{item_id}.csv'
    if os.path.exists(file_path):
        existing_links.append((item_id, link))
    else:
        new_links.append((item_id, link))

prioritized_list = new_links + existing_links

# Warm the engines for scraping

# Setting a realistic user agent
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"

# Configure Chrome Options for Headless Mode
options = Options()
options.add_argument(f'user-agent={user_agent}')
options.add_argument("--no-sandbox")  # Bypass OS security model, necessary for Docker and certain CI environments
options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
options.add_argument("--disable-gpu")  # Applicable to windows os only
options.add_argument("--disable-setuid-sandbox")

# Initialize Selenium WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Define get_item_details function
def get_item_details(link, item_id):
    print(f'Getting details for item {item_id}')

    driver.get(link)
    time.sleep(random.uniform(8, 10))
    
    # Get hardcoded JSON
    def extract_json():
        # Find the script tag containing the specific text
        target_text = "window.goodsDetailV3SsrData"
        script_tags = driver.find_elements(By.TAG_NAME, "script")
        for script_tag in script_tags:
            try:
                script_content = script_tag.get_attribute('innerHTML')
                if target_text in script_content:
                    match = re.search(r'{.*}', script_content)
                    if match:
                        return json.loads(match.group(0))
            except Exception as e:
                print(f'Did not find <script> for item {item_id}: {e}')
        return {}

    # Get JSON from script tag
    parsed_json = extract_json()
    
    # Get Title
    try:
        h1 = driver.find_element(By.TAG_NAME, 'h1')

        if h1:
           title = h1.text
        else:
            print(f'Could not get <h1> for item {item_id}')
            titleElement = driver.find_element(By.TAG_NAME, 'title')

            if titleElement:
                title = titleElement.text.split('|')[0].strip()
            else:
                print(f'Could not get <title> for item {item_id}')

    except Exception:
        title = "" 
    
    # Get Image
    try:
        img_tag = driver.find_element(By.CSS_SELECTOR, "img[data-src]")
        image = img_tag.get_attribute('data-src')
        if image.startswith('//'):
            image = 'https:' + image
    except Exception:
        image = ""
    
    # Get Price
    # try:
    #     price_element = driver.find_element(By.CSS_SELECTOR, ".product-intro__head-mainprice [aria-label]")
    #     price_text = price_element.text
    #     # Remove currency symbols and convert to float
    #     price = float(re.sub(r'[^\d.]+', '', price_text))
    # except Exception:
    #     price = ""

    # Get SKU
    try:
        sku = parsed_json["rs"]["detail"]["goods_sn"]
    except Exception:
        sku = ""  # Set to an empty string in case of any error

    # Get Composition
    composition_values = []
    
    def extract_detail_from_json(parsed_json):
        # Check if the expected data structure exists and return details
        if 'productIntroData' in parsed_json:
            if 'detail' in parsed_json['productIntroData']:
                detail = parsed_json['productIntroData']['detail']
                return detail
            else:
                print(f'Did not find `detail` in JSON for item ID: {link}')    
        else:
            print(f'Did not find `productIntroData` in JSON for item ID: {link}')
            return None

    detail = extract_detail_from_json(parsed_json)

    # Functions for getting price
    def get_lowest_price(detail):
        def try_float(value):
            try:
                value = float(value)
                return value if value != 0 else None
            except (TypeError, ValueError):
                return None
        
        retail_price = detail.get('retailPrice', {}).get('usdAmount', None)
        sale_price = detail.get('salePrice', {}).get('usdAmount', None)

        # Convert to float and filter out None and 0 values
        prices = filter(None, [try_float(retail_price), try_float(sale_price)])

        # Return the minimum price if available, else None
        return min(prices, default=None)

    # Set some properties as empty strings by default
    price = ""
    Type = "" 

    if detail:

        # Get price
        price = get_lowest_price(detail)

        if "cat_id" in detail:

            # Get category
            Type = detail["cat_id"]

        if 'multiPartInfo' in detail:
            for item in detail['multiPartInfo']:
                if 'attributeList'in item:
                    for attribute in item['attributeList']:
                        if 'attr_name_en' in attribute and attribute['attr_name_en'] == 'Composition':
                            composition_values.append(attribute.get('attr_value_en', ''))

        if 'productDetails' in detail:
            for item in detail['productDetails']:
                if 'attr_name_en' in item and item['attr_name_en'] == 'Composition':
                    composition_values.append(item.get('attr_value_en', ''))

    composition = ', '.join(composition_values) if composition_values else ''

    # Check if required fields are present
    if title and composition and image and sku:
        
        # Get Timestamp
        timestamp = datetime.datetime.now()
        
        # Include the item name in the details
        item_details = [[title, composition, price, image, timestamp, sku, link, Type]]
            
        # Creating DataFrame
        df = pd.DataFrame(item_details, columns=['Title', 'Composition', 'Price', 'Image', 'Timestamp', 'SKU', 'Link', 'Type'])

        # Save to CSV
        df.to_csv(f"{output_folder}{item_id}.csv", index=False)
        print(f'Saved item {item_id}')

    else:
        if not title:
            print(f'Could not get title for item {item_id}')
        if not composition:
            print(f'Could not get composition for item {item_id}')
        if not image:
            print(f'Could not get image for item {item_id}')
        if not sku:
            print(f'Could not get image for item {item_id}')


# Create a new directory 'items' if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Get all items details
for item_id, link in prioritized_list[:limit]:
    get_item_details(link, item_id)

driver.quit() # Close the browser