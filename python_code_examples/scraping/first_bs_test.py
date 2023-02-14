"""A first simple test-run of the BeautifulSoup module, using
   a simple web page created just for this purpose.
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

# open a web page file
page = urlopen("https://weimergeeks.com/examples/scraping/example1.html")

# parse that to create a BeautifulSoup object
soup = BeautifulSoup(page, "html.parser")

# print the first H1 element in the file
print(soup.h1)

# print ONLY THE TEXT in the first H1 element in the file
print(soup.h1.text)

# get all the TD elements that have the class 'city'
city_list = soup.find_all( "td", class_="city" )

# print only the text from each of those TD elements
for city in city_list:
    print( city.text )

# using find() gets only ONE element
# here we assign that element to a new variable, phone_number
phone_number = soup.find( id="call" )

# print only the text from the element with the id 'call'
print( phone_number.text )

# get the values of all the src attributes for all the IMG elements
# on the web page, and print them, one per line
image_list = soup.find_all('img')
for image in image_list:
    print( image.attrs['src'] )
