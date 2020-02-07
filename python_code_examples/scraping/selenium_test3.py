import time
from selenium import webdriver
from random import randint
from bs4 import BeautifulSoup


# my path is '/Users/mcadams/Documents/python/'
# yours will be different


# load your driver
driver = webdriver.Chrome('/Users/mcadams/Documents/python/chromedriver')

# get the web page
driver.get('https://www.rottentomatoes.com/browse/dvd-streaming-all');

# click the button exactly 8 times
for n in range(8):
    driver.find_element_by_css_selector('.btn.btn-secondary-rt.mb-load-btn').click()
    # the button tag has class="btn btn-secondary-rt mb-load-btn"
    # ... we told it which button to click
    # make a random wait time between 1 and 10 seconds to look less bot-like
    s = randint(1, 10)
    # sleep that number of seconds
    time.sleep(s)

page = driver.page_source

soup = BeautifulSoup(page, "html.parser")
title_list = soup.find_all("h3", class_="movieTitle")
for title in title_list:
    print(title.get_text())

print("There are " + str(len(title_list)) + " movies in the list.")

driver.quit()
