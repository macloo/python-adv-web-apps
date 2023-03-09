# chromedriver test Feb. 2023
#
# This requires Selenium to be installed in your virtualenv
# And you need to download and install chromedriver as explained here:
# http://bit.ly/selenium-intro

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# open page
driver.get('http://www.google.com/');
# find the search box
search_box = driver.find_element("name", "q")
# type 'ChromeDriver' into the search box
search_box.send_keys('ChromeDriver')

# submit the text - typical Google search - see search results appear
time.sleep(5) # let the user actually see something!
search_box.submit()
time.sleep(5) # let the user actually see something!

driver.quit()
