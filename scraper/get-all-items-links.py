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

base_url = "https://us.shein.com/hotsale/Women-top-rated-sc-003161153.html?adp=20527159&categoryJump=true&ici=us_tab01navbar03menu01dir03&src_identifier=fc%3DAll%60sc%3DWomenClothing%60tc%3D0%60oc%3DToprated%60ps%3Dtab01navbar03menu01dir03%60jc%3DitemPicking_003161153&src_module=topcat&src_tab_page_id=page_real_class1697808447511&child_cat_id=1766"

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

def scrape_links(url):
    driver.get(url)
    time.sleep(random.uniform(12, 24))
    elements = driver.find_elements(By.CSS_SELECTOR, 'a')
    
    # Specify the class you are interested in
    desired_class = 'goods-title-link'

    # Filter elements that contain the specified class
    elements = [element for element in elements if desired_class in element.get_attribute('class')]
    
    links = []
    for element in elements:
        # Get the core part of the href
        href_full = element.get_attribute('href')
        href = href_full.split('?')[0]

        # Extract the ID using regex
        match = re.search(r'-p-(\d+)\.html', href)
        if match:
            id = match.group(1)
        else:
            id = None

        timestamp = datetime.datetime.now()

        links.append((id, href, timestamp))

    return links

all_links = []
min_links_to_save = 2

# Get random page from 1 to 10
page_number = random.randint(1,10)

while True:
    current_url = f"{base_url}&page={page_number}"
    links = scrape_links(current_url)

    print(f"Page {page_number} has {len(links)} links")

    if not links:
        break

    all_links.extend(links)
    page_number += 1
    time.sleep(random.uniform(1, 2)) # Pause to mimic human browsing

driver.quit()  # Close the browser

# Creating DataFrame
df = pd.DataFrame(all_links, columns=['Item ID', 'Link', 'Timestamp'])

if len(all_links) >= min_links_to_save:
    # Create a new directory 'scraper/links' if it doesn't exist
    os.makedirs('scraper/links', exist_ok=True)

    # Define file name using the current timestamp
    filename = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

    # Save to CSV
    df.to_csv(f"scraper/links/{filename}.csv", index=False)
else:
    print(f"Not enough items to save. Need at least { min_links_to_save }, got:", len(all_links))