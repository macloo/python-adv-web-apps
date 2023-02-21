from bs4 import BeautifulSoup
import requests

url = "https://en.wikipedia.org/wiki/List_of_Scottish_monarchs"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

# get all tables in the article
tables = soup.find_all( 'table', class_='wikitable' )

# new empty list
kings = []

# loop over all tables, get all kings, print each and add it to the list
for table in tables:
    rows = table.find_all('tr')
    for row in rows:
        try:
            cells = row.find_all('td')
            # print contents of the first cell in the row
            print( cells[0].text.strip() )
            # add text to list - this is the complete contents of the cell
            kings.append( cells[0].text.strip() )
        except:
            pass

# how many kings?
print("Number of kings: " + str(len(kings)))
