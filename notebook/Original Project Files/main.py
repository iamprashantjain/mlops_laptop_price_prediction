from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import random
import time


# Initialize Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration
chrome_options.add_argument("--no-sandbox")  # No sandboxing for headless mode
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

# Initialize the Chrome WebDriver service
service = Service(r"H:\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

# Navigate to the desired URL
driver.get('https://www.smartprix.com/laptops')

# Initialize WebDriverWait
wait = WebDriverWait(driver, 10)

# Initialize data storage
data = {
    'Name': [],
    'Price': [],
    'Discount': [],
    'Rating': [],
    'Rating Count': [],
    'Spec Score': [],
    'Features': [],
    'Link': [],
    'Image URL': []
}

def extract_data(soup):
    """ Extract data from BeautifulSoup object """
    for product in soup.find_all('div', class_='sm-product'):
        try:
            name_tag = product.find('a', class_='name')
            price_tag = product.find('span', class_='price')
            discount_tag = product.find('span', class_='sm-pdrop')
            rating_tag = product.find('span', class_='sm-rating')
            rating_count_tag = product.find('div', class_='rating')
            spec_score_tag = product.find('div', class_='score')
            features_tag = product.find('ul', class_='sm-feat specs')

            # Extract text and attributes
            name = name_tag.text.strip() if name_tag else 'N/A'
            price = price_tag.text.strip() if price_tag else 'N/A'
            discount = discount_tag.text.strip() if discount_tag else 'N/A'
            rating = rating_tag['style'].split(':')[1].strip() if rating_tag and 'style' in rating_tag.attrs else 'N/A'
            rating_count = rating_count_tag.text.strip() if rating_count_tag else 'N/A'
            spec_score = spec_score_tag.get_text(strip=True).split()[0] if spec_score_tag else 'N/A'
            features = ', '.join([li.text for li in features_tag.find_all('li')]) if features_tag else 'N/A'
        except Exception as e:
            print(f"Error extracting data from product: {e}")
            name = 'Error'
            price = 'Error'
            discount = 'Error'
            rating = 'Error'
            rating_count = 'Error'
            spec_score = 'Error'
            features = 'Error'

        # Append data to lists
        data['Name'].append(name)
        data['Price'].append(price)
        data['Discount'].append(discount)
        data['Rating'].append(rating)
        data['Rating Count'].append(rating_count)
        data['Spec Score'].append(spec_score)
        data['Features'].append(features)
        data['Link'].append('')
        data['Image URL'].append('')

def check_for_503_error():
    """Check if the current page is giving a 503 error."""
    try:
        # Using JavaScript to fetch the status code from the network (if available)
        status_code = driver.execute_script("return window.performance.getEntriesByType('navigation')[0].responseStart;")
        if status_code == 503:
            print("Received HTTP 503 error")
            return True
    except Exception as e:
        print(f"Error checking for 503 error: {e}")
    return False

# Click "Load More" button and extract data
while True:
    try:
        # Extract data before clicking "Load More"
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        extract_data(soup)
        
        # Check for HTTP 503 error
        if check_for_503_error():
            break

        try:
            # Click "Load More" button
            load_more_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/main/div[1]/div[3]/div[3]")))
            load_more_button.click()
            
            print("Clicked 'Load More' button")
        
        except Exception as e:
            print(f"No Load More button or error: {e}")
            break
        
        # Wait for new content to load
        time.sleep(random.uniform(2, 7))
    
    except Exception as e:
        print(f"Error occurred: {e}")
        break



    # Create DataFrame from data
    df = pd.DataFrame(data)
    
    final_df = pd.concat(final_df, df)
    
    

import pdb
pdb.set_trace()