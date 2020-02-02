from bs4 import BeautifulSoup
import requests

start = "https://xkcd.com/2260/"
page = requests.get(start)
soup = BeautifulSoup(page.text, 'html.parser')

prevLink = soup.select('a[rel="prev"]')[0]
print(prevLink)

print( prevLink.get('href') )

url = 'https://xkcd.com' + prevLink.get('href')
print(url)
