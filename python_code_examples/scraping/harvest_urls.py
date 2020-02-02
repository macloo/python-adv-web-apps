"""scrape all the URLs from the article segment of a Wikipedia page
   and write them into a plain-text file - gets all links - even
   those that begin with #
"""

from bs4 import BeautifulSoup
import requests

# get the contents of one page
start = 'http://en.wikipedia.org/wiki/Harrison_Ford'
page = requests.get(start)
soup = BeautifulSoup(page.text, 'html.parser')

# name the text file that will be created or overwritten
filename = 'myfile.txt'

def capture_urls(filename, soup):
    """harvest the URLs and write them to file"""
    # create and open the file for writing - note, with 'w' this will
    # delete all contents of the file if it already exists
    myfile = open(filename, 'w')

    # get all contents of only the article
    article = soup.find(id='mw-content-text')

    # get all <a> elements
    links_list = article.find_all('a')

    # get contents of all href='' attributes with a loop
    for link in links_list:
        if 'href' in link.attrs:
            # write one href into the text file - '\n' is newline
            myfile.write(link.attrs['href'] + '\n')

    # close and save the file after loop ends
    myfile.close()

# call the function
capture_urls(filename, soup)
