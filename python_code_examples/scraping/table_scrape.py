from bs4 import BeautifulSoup
import requests

url = "https://en.wikipedia.org/wiki/List_of_Scottish_monarchs"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

# get the first table in the article
table = soup.find( 'table', class_='wikitable' )

# get a list of all rows in that table
rows = table.find_all('tr')

# loop over all rows, get all cells
for row in rows:
    try:
        cells = row.find_all('td')
        # print contents of the first cell in the row
        print( cells[0].text )
    except:
        pass
