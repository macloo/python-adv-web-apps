"""
Functions we can import
"""

import csv

def convert_to_dict(filename):
    """
    Convert a CSV file to a list of Python dictionaries.
    """
    # open a CSV file - note - must have column headings in top row
    datafile = open(filename, newline='')

    # create list of OrderedDicts as of Python 3.6
    my_reader = csv.DictReader(datafile)

    # write it all out to a new list
    list_of_dicts = []
    for row in my_reader:
        # we convert each row to a string and add a newline
        list_of_dicts.append( dict(row) )

    # close original csv file
    datafile.close()
    # return the list
    return list_of_dicts


def make_ordinal(num):
    """
    Create an ordinal (1st, 2nd, etc.) from a number.
    """
    base = num % 10
    if base in [0,4,5,6,7,8,9] or num in [11,12,13]:
        ext = "th"
    elif base == 1:
        ext = "st"
    elif base == 2:
        ext = "nd"
    else:
        ext = "rd"
    return str(num) + ext

# tests
def test_make_ordinal():
    for i in range(1,46):
        print(make_ordinal(i))

def search_the_list(list):
    for item in list:
        if "Whig" in item['Party']:
            print(item['President'] + " was a Whig.")
    for k in list[0].keys():
        print(k)

# run tests
if __name__ == '__main__':
    test_make_ordinal()
    presidents_list = convert_to_dict("presidents.csv")
    search_the_list(presidents_list)
    print(make_ordinal(12))
    print(make_ordinal(32))
