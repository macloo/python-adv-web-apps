# tested Feb. 2025

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup
from random import randint
import time

# load the driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# get the web page
driver.get('https://www.rottentomatoes.com/browse/movies_at_home/');

# click the button exactly 8 times to load more movies
for n in range(8):
    button = driver.find_element(By.CLASS_NAME, "discovery__actions").find_element(By.TAG_NAME, "button")
    button.click()
    # ... we told it which button to click
    # make a random wait time between 1 and 10 seconds to look less bot-like
    s = randint(1, 10)
    # sleep that number of seconds
    time.sleep(s)

# page_source is a variable created by Selenium - it holds all the HTML
page = driver.page_source

soup = BeautifulSoup(page, "html.parser")
# each tile contains all info for one movie
tiles = soup.find_all('a', class_="js-tile-link")

movie_titles = []

for tile in tiles:
    span = tile.find('span', class_="p--small")
    title = span.text.strip()
    if len(title) > 0:
        movie_titles.append( title )
        print( title )

print("There are " + str( len(movie_titles) ) + " movies in the list.")

driver.quit()
