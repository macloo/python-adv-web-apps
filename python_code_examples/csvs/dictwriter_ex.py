"""template script for creating a csv file from a dictionary"""
import csv

# sample of a list of dictionaries
# normally this would be in a separate file, or
# constructed from data in a separate file
presidents_list = [
{"Presidency":1,"President":"George Washington","Wikipedia_entry":"http://en.wikipedia.org/wiki/George_Washington","Took_office":"4/30/1789","Left_office":"3/4/1797","Party":"Independent ","Home_state":"Virginia","Occupation":"Planter","College":"None","Age_when_took_office":57,"Birth_date":"2/22/1732","Birthplace":"Westmoreland County, Virginia","Death_date":"12/14/1799","Location_death":"Mount Vernon, Virginia"},
{"Presidency":2,"President":"John Adams","Wikipedia_entry":"http://en.wikipedia.org/wiki/John_Adams","Took_office":"3/4/1797","Left_office":"3/4/1801","Party":"Federalist ","Home_state":"Massachusetts","Occupation":"Lawyer","College":"Harvard","Age_when_took_office":61,"Birth_date":"10/30/1735","Birthplace":"Quincy, Massachusetts","Death_date":"7/4/1826","Location_death":"Quincy, Massachusetts"},
{"Presidency":3,"President":"Thomas Jefferson","Wikipedia_entry":"http://en.wikipedia.org/wiki/Thomas_Jefferson","Took_office":"3/4/1801","Left_office":"3/4/1809","Party":"Democratic-Republican ","Home_state":"Virginia","Occupation":"Planter, Lawyer","College":"William and Mary","Age_when_took_office":57,"Birth_date":"4/13/1743","Birthplace":"Albemarle County, Virginia","Death_date":"7/4/1826","Location_death":"Albemarle County, Virginia"},
{"Presidency":4,"President":"James Madison","Wikipedia_entry":"http://en.wikipedia.org/wiki/James_Madison","Took_office":"3/4/1809","Left_office":"3/4/1817","Party":"Democratic-Republican ","Home_state":"Virginia","Occupation":"Lawyer","College":"Princeton","Age_when_took_office":57,"Birth_date":"3/16/1751","Birthplace":"Port Conway, Virginia","Death_date":"6/28/1836","Location_death":"Orange County, Virginia"},
{"Presidency":5,"President":"James Monroe","Wikipedia_entry":"http://en.wikipedia.org/wiki/James_Monroe","Took_office":"3/4/1817","Left_office":"3/4/1825","Party":"Democratic-Republican ","Home_state":"Virginia","Occupation":"Lawyer","College":"William and Mary","Age_when_took_office":58,"Birth_date":"4/28/1758","Birthplace":"Westmoreland County, Virginia","Death_date":"7/4/1831","Location_death":"New York, New York"}
]

# open a new file for writing - if file exists, contents will be erased
csvfile = open('new_file.csv', 'w')

# set the headers
headers = ['Presidency', 'President', 'Wikipedia_entry', 'Took_office', 'Left_office', 'Party', 'Home_state', 'Occupation', 'College', 'Age_when_took_office', 'Birth_date', 'Birthplace', 'Death_date', 'Location_death']

# make a new variable - c - for Python's DictWriter object -
# note that fieldnames is required
c = csv.DictWriter(csvfile, fieldnames=headers)

# optional - write a header row
c.writeheader()

# write all rows from list to file
c.writerows(presidents_list)

# save and close file
csvfile.close()
