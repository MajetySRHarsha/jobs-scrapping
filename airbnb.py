from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from database import insert_to_table

chrome_options = Options()
chrome_options.add_argument('--headless')  # Run Chrome in headless mode (no visible browser window)
chrome_options.add_argument('--disable-gpu')  # Disable GPU acceleration

# Initialize the ChromeDriver
driver = webdriver.Chrome(options=chrome_options)

try:
    # Navigate to the URL with dynamic content
    driver.get('https://careers.airbnb.com/university/')

    # Wait for the dynamic content to load (adjust the time according to your needs)
    wait = WebDriverWait(driver, 10)
    dynamic_elements = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'jobs-board__positions__list__item')))
    dynamic_links = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'jobs-board__positions__list__item__link')))
    dynamic_place=wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'jobs-board__positions__list__item__location')))
    # Extract the data
    scraped_data = [element.text for element in dynamic_elements]
    scraped_links = [element.get_attribute('href') for element in dynamic_links]
    scraped_place=[element.text for element in dynamic_place]

    # Do something with the scraped data (printing in this example)
    for title in scraped_data:
        print(title)
    for link in scraped_links:
        print(link)
    for location in scraped_place:
        print(location)
    for i in range(len(scraped_data)):
        insert_to_table(scraped_data[i],scraped_place[i],scraped_links[i],'Intern','Airbnb')

finally:
    # Close the browser after scraping
    driver.quit()