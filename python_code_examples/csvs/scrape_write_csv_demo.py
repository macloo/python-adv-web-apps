"""example script for scraping a table and writing the data to a CSV file"""

import csv

import requests
from bs4 import BeautifulSoup
page = requests.get("https://weimergeeks.com/examples/scraping/example1.html")
soup = BeautifulSoup(page.text, 'html.parser')

# open new file for writing -
csvfile = open('table_scrape.csv', 'w', newline='', encoding='utf-8')

# make a new variable - c - for Python's CSV writer object -
c = csv.writer(csvfile)

# there is only one table on this page - get it with find()
table = soup.find('table')

# get all rows from table
rows = table.find_all("tr")

# loop over all the rows
for row in rows:
    # a temporary list that will be overwritten each time the loop runs
    tmp_row = []
    # get all cells from row
    cells = row.find_all('td')
    # loop over all the td's in the current row - a loop inside a loop
    for cell in cells:
        # add contents of one td (cell) to the list
        tmp_row.append( cell.text )
    # when all cells in one row have been added to the list,
    # write one new row to the csv
    c.writerow(tmp_row)

# close the file
csvfile.close()
