"""Scrape info about the five top-grossing movies for each year,
    for 10 years. Get the title and rank of the movie, the year, and
    how much money it grossed at the box office. Put the scraped data
    into a CSV file.
"""

from bs4 import BeautifulSoup
import requests
import csv

def build_years_list(start):
    """create a list of 10 years counting backward from the start year"""
    years = []
    for i in range(0, 10):
        years.append(start - i)
    return years

years = build_years_list(2019)

# create a base url
base_url = 'https://www.boxofficemojo.com/year/'

# open new file for writing - this creates the file
csvfile = open("movies.csv", 'w', newline='', encoding='utf-8')

# make a new variable, c, for Python's CSV writer object -
c = csv.writer(csvfile)

# write a header row to the csv
c.writerow( ['year', 'rank', 'title', 'gross'] )

# scraper code for top five movies, 10 years
for year in years:
    url = base_url + str(year) + "/"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    table = soup.find( 'table' )
    rows = table.find_all('tr')
    # for each row that was read, write one row to the CSV file
    for i in range(1, 6):
        cells = rows[i].find_all('td')
        gross = cells[7].text.strip('$').replace(',', '')
        c.writerow( [year, cells[0].text, cells[1].text, gross] )

# close the file
csvfile.close()

print("The CSV is done!")
