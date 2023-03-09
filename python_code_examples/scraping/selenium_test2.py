# tested Feb. 2023

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from bs4 import BeautifulSoup

# load the driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# get the web page
driver.get('https://www.rottentomatoes.com/browse/movies_at_home/');

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
