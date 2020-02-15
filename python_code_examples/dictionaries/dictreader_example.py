import csv

# open a CSV file
# note - the CSV must have column headings in top row
datafile = open("sample.csv", newline='')

# create a dictReader object
my_reader = csv.DictReader(datafile)

for row in my_reader:
    print(row['Year'], row['Author'], row['Title'])

datafile.close()
