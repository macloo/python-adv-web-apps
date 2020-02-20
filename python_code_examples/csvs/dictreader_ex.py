"""template script for creating a dict from a csv file"""
import csv

# open an existing file for reading -
csvfile = open('presidents.csv', newline='')

# make a new variable - c - for Python's DictReader object -
c = csv.DictReader(csvfile)

# read whatever you want from the DictReader object
# using the column headings from the CSV as the dict keys
for row in c:
    print(row['President'] + " ... " + row['Party'])

# save and close the file
csvfile.close()
