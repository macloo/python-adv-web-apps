"""modified scraper to get multiple URLs from multiple pages.
   Original files at https://github.com/macloo/web-scraper-steps
   This script scrapes URLs only.
"""

from bs4 import BeautifulSoup
import requests

# get first page that lists players
start = 'https://www.mlssoccer.com/players'
page = requests.get(start)
soup = BeautifulSoup(page.text, 'html.parser')

# new list to contain all player page URLs
player_list = []

def get_next_page(soup):
    """get link to next page"""
    next_page = soup.find( 'a', title='Go to next page' )
    if next_page and ('href' in next_page.attrs):
        partial = next_page.attrs['href']
        new_url = 'https://www.mlssoccer.com' + partial
        # get the next page, open it, make soup
        new_page = requests.get(new_url)
        new_soup = BeautifulSoup(new_page.text, 'html.parser')
        return new_soup
    else:
        print("Done collecting URLs ...")
        return None

def get_player_pages(soup, player_list):
    """scrape URLs from one page"""
    tag_list = soup.find_all( 'a', class_='row_link' )
    for tag in tag_list:
        if 'href' in tag.attrs:
            player_list.append(tag.attrs['href'])
    return player_list

# scrape all until done
while soup:
    # get all player URLs from one list page
    player_list = get_player_pages(soup, player_list)
    # go to next list page, make new soup
    soup = get_next_page(soup)

# proof that all URLs are in the list now
for index, item in enumerate(player_list):
    print(index, item)
