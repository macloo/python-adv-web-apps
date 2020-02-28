"""version 2 of a modified scraper to get multiple URLs
   from multiple pages.
   Original files at https://github.com/macloo/web-scraper-steps
   This script scrapes URLs only.

   -- Difference between this script and mls_pages.py --
   Here we simply look at the URL of the last page of all
   list pages and examine its URL:

   https://www.mlssoccer.com/players?page=23

   We use that number, 23, to build URLs for all list pages.
"""

from bs4 import BeautifulSoup
import requests

# get first page that lists players
url = 'https://www.mlssoccer.com/players'

# new list to contain all player page URLs
player_list = []

def get_player_pages(soup, player_list):
    """scrape URLs from one page"""
    tag_list = soup.find_all( 'a', class_='row_link' )
    for tag in tag_list:
        if 'href' in tag.attrs:
            player_list.append(tag.attrs['href'])
    return player_list

# scrape all until done
# note, the first iteration of the loop uses url as defined above
for i in range(24):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    player_list = get_player_pages(soup, player_list)
    # example - https://www.mlssoccer.com/players?page=23
    url = 'https://www.mlssoccer.com/players?page=' + str(i + 1)

# proof that all URLs are in the list now
for index, item in enumerate(player_list):
    print(index, item)
