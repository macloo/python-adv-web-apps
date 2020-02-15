"""
convert a csv file to dictionaries - each row is one dict
Python 3.6 and not before
"""
import csv

# open a CSV file
# note - must have column headings in top row
datafile = open("sample.csv", newline='')

# create list of OrderedDicts as of Python 3.6
my_reader = csv.DictReader(datafile)


# commented out because both loops can't run
#    - this works -
# my_list = []
# for row in my_reader:
#     my_list.append( dict(row) )
#
# print(my_list[1]["Title"])


# write it all out to a new file
targetfile = open("newdict.py", 'w')
for row in my_reader:
    # we convert each row to a string and add a newline
    targetfile.write( str(dict(row)) + "\n" )
targetfile.close()


# close original csv file
datafile.close()
