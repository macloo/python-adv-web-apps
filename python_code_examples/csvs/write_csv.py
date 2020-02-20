"""template script for writing to a csv file"""
import csv

# open new file for writing - will erase file if it already exists -
csvfile = open('example.csv', 'w', newline='', encoding='utf-8')

# make a new variable - c - for Python's CSV writer object -
c = csv.writer(csvfile)

# write a column headings row - do this only once -
c.writerow( ['name','address','job'] )

# call some function that returns a list --
# for purposes of the template, here is a list of lists -
the_list = [
    ['Alice', 'Gainesville, Florida', 'chef'],
    ['Bob', 'Chicago, Illinois', 'writer'],
    ['Ted', 'Miami, Florida', 'driver'],
    ['Carol', 'Portland, Oregon', 'executive']
]

# use a for-loop to write each row into the CSV file
for item in the_list:
    # write one row to csv — item MUST BE a LIST
    c.writerow(item)

# save and close the file
csvfile.close()
