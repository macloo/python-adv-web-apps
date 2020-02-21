""" template script for writing to a csv file using `with` """
import csv

with open('example2.csv', 'w', newline='') as csvfile:
    c = csv.writer(csvfile)
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

# DO NOT ADD csvfile.close()
