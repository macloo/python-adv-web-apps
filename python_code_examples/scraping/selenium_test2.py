from selenium import webdriver
from bs4 import BeautifulSoup


# my path is '/Users/mcadams/Documents/python/'
# yours will be different


# load your driver
driver = webdriver.Chrome('/Users/mcadams/Documents/python/chromedriver')

# get the web page
driver.get('https://www.rottentomatoes.com/browse/dvd-streaming-all');

# page_source is a variable created by Selenium - it holds all the HTML
page = driver.page_source

soup = BeautifulSoup(page, "html.parser")
title_list = soup.find_all("h3", class_="movieTitle")
for title in title_list:
    print(title.get_text())

print("There are " + str(len(title_list)) + " movies in the list.")

driver.quit()
