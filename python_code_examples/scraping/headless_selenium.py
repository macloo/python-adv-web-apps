# tested February 2025
# run Selenium without seeing the browser

from selenium import webdriver

# new headless stuff
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless=new")
driver = webdriver.Chrome(options=chrome_options)

from bs4 import BeautifulSoup

# fill in URL for page you want to scrape
driver.get('https://en.wikipedia.org/wiki/Antarctica');

page = driver.page_source
soup = BeautifulSoup(page, 'html.parser')

# example of scraping from one page - h2s and h3s
heds = soup.find_all('div', class_="mw-heading")

for hed in heds:
    print( hed.text )

print("There are " + str( len(heds) ) + " headings in the list.")

driver.quit()
