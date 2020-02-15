"""convert a csv file to dictionaries - each row is one dict
    in a single Python list
    Python 3.6 and later
"""
import csv

# open a CSV file
# note - the CSV must have column headings in top row
datafile = open("sample.csv", newline='')

# create list of OrderedDicts - as of Python 3.6
my_reader = csv.DictReader(datafile)

# crerate new empty list
my_list = []

# loop over CSV row by row and write each row as a dictionary into the list
for row in my_reader:
    my_list.append( dict(row) )

# print some examples from the new list
print("Printing second item:")
print(my_list[1])
print("What is the data tyoe of the item?")
print(type(my_list[1]))
print("Printing value of key \"Title\" for second item:")
print(my_list[1]["Title"])
print("Printing value of key \"Author\" for second item:")
print(my_list[1]["Author"])

# close original csv file
datafile.close()
