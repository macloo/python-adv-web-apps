# chromedriver - tested Feb. 2025
#
# This requires Selenium to be installed in your virtualenv
# And you need to download and install chromedriver as explained here:
# http://bit.ly/selenium-intro

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# open a page
driver.get('http://www.google.com/');
# find the Google search box
search_box = driver.find_element("name", "q")
# type text into the search box
search_box.send_keys('elephants')
# wait 5 seconds, time to let the user see the text
time.sleep(5)
search_box.submit()
# let the user see the result! 30 seconds, then quit
time.sleep(30)
# close the instance of Chrome opened by this script
driver.quit()
