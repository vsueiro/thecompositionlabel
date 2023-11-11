from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests
import pandas as pd
import random
import time
import datetime
import os

base_url = "https://us.shein.com/hotsale/Women-top-rated-sc-003161153.html?adp=20527159&categoryJump=true&ici=us_tab01navbar03menu01dir03&src_identifier=fc%3DAll%60sc%3DWomenClothing%60tc%3D0%60oc%3DToprated%60ps%3Dtab01navbar03menu01dir03%60jc%3DitemPicking_003161153&src_module=topcat&src_tab_page_id=page_real_class1697808447511&child_cat_id=1766"

def scrape_links(url):
    headers = {
        'User-Agent': get_random_user_agent()
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    links = [(urljoin(url, a['href']), datetime.datetime.now()) for a in soup.find_all('a', class_='S-product-item__link')]
    return links

# Function to get a random User-Agent
def get_random_user_agent():
    user_agents = [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Safari/605.1.15',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Safari/606.1.25',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Brave/1.0.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Brave/1.15.75',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Brave/1.17.73',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/18.18363',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/89.0.774.77',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/91.0.864.48',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/58.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/65.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/70.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/80.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Opera/64.0.3417.54',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Opera/75.0.3941.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Opera/80.0.3987.163',
    ]

    return random.choice(user_agents)

all_links = []
page_number = 4

while True:

    current_url = f"{base_url}&page={page_number}"
    links = scrape_links(current_url)
    
    print(f"Page {page_number} has {len(links)} links")
    
    if not links:
        break

    all_links.extend(links)
    page_number += 1
    time.sleep(10)

# Creating DataFrame
df = pd.DataFrame(all_links, columns=['Link', 'Timestamp'])

# Create a new directory 'links' if it doesn't exist
os.makedirs('links', exist_ok=True)

# Define file name
filename = datetime.datetime.now()

# Save to CSV
df.to_csv(f"links/{filename}.csv", index=False)
