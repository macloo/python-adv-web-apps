# from https://sites.google.com/a/chromium.org/chromedriver/getting-started
# 
# This requires Selenium to be installed in your virtualenv
# And you need to download and install chromedriver as explained here:
# http://bit.ly/selenium-intro

import time
from selenium import webdriver

# driver = webdriver.Chrome('/path/to/chromedriver')
# NOTE this is my own path, not yours --
driver = webdriver.Chrome('/Users/mcadams/Documents/python/chromedriver')

driver.get('http://www.google.com/')
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!

driver.quit()
