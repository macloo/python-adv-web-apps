"""template script for reading from a csv file"""
import csv

# open an existing file for reading -
csvfile = open('presidents.csv')

# make a new variable - c - for Python's CSV reader object -
c = csv.reader(csvfile)

# read whatever you want from the reader object
# print it or use it any way you like
for row in c:
    print( row[1] + ", " + row[5])

# save and close the file
csvfile.close()
