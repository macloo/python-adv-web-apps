"""convert a csv file to dictionaries - each row is one dict
    in this example, we print each dict value as a string
    Python 3.6 and later
"""
import csv

# open a CSV file
# note - the CSV must have column headings in top row
datafile = open("sample.csv", newline='')

# create list of OrderedDicts - as of Python 3.6
my_reader = csv.DictReader(datafile)

# print all the dictionaries as text strings
for row in my_reader:
    # plug each value from the row into a string
    print( row['Title'] + ', by ' + row['Author'] + ' (' + row['Year'] + ')' )

# blank line
print()

# close original csv file
datafile.close()
