"""example script for scraping a table and writing the data to a new CSV file"""

import csv

import requests
from bs4 import BeautifulSoup
page = requests.get("https://weimergeeks.com/examples/scraping/example1.html")
soup = BeautifulSoup(page.text, 'html.parser')

# open new empty file for writing -
csvfile = open('table_scrape.csv', 'w', newline='', encoding='utf-8')

# make a new variable - c - for Python's CSV writer object -
c = csv.writer(csvfile)

# write a header row to the CSV file
c.writerow( ['Capital City', 'Country'] )

# there is only one table on this page - so get it with find()
table = soup.find('table')

# get all rows from table
rows = table.find_all("tr")

# loop over all the rows
for row in rows:
    # a temporary list that will be overwritten each time the loop runs
    tmp_row = []
    # get all cells from one row
    cells = row.find_all('td')
    # loop over all the td's in the current row - a loop inside a loop
    for cell in cells:
        # add contents of one td (cell) to the list
        tmp_row.append( cell.text )
    # after all cells in one row have been added to the list,
    # write that one row to the csv - 
    # then the loop will run again as long as there are rows left
    c.writerow(tmp_row)

# close the file
csvfile.close()
