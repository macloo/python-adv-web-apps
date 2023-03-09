import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

chrome_options = Options()
chrome_options.add_argument("--headless")
# fill in your own path to installed chromedriver
driver = webdriver.Chrome( executable_path=
            '/Users/dirname/dirname/dirname//chromedriver',
            options=chrome_options )

# fill in URL for page you want to scrape
driver.get('https://somedomain.com');

time.sleep(2)

page = driver.page_source

soup = BeautifulSoup(page, 'html.parser')

h1_list = soup.find_all('h1')
print(h1_list)

driver.quit()
