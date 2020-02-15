# here is a complex dataset - 4 Python dictionaries are in a Python list
# the dictionaries also have dictionaries INSIDE THEM: name, location, and
# picture are KEYS that each have a dictionary as their VALUE
# note there are only 4 list items, and each one is a dictionary of data
# about one (fictitious) person

data = [
{"gender":"female","name":{"title":"miss","first":"heather","last":"hale"},"location":{"street":"5655 shady ln dr","city":"pasadena","state":"missouri","postcode":85370},"dob":"1966-12-08 08:12:49","id":{"name":"SSN","value":"470-06-2694"},"picture":{"large":"https://randomuser.me/api/portraits/women/35.jpg","medium":"https://randomuser.me/api/portraits/med/women/35.jpg","thumbnail":"https://randomuser.me/api/portraits/thumb/women/35.jpg"}},
{"gender":"female","name":{"title":"miss","first":"sofia","last":"howard"},"location":{"street":"9807 central st","city":"thousand oaks","state":"colorado","postcode":75029},"dob":"1953-07-13 06:57:13","id":{"name":"SSN","value":"493-62-4484"},"picture":{"large":"https://randomuser.me/api/portraits/women/48.jpg","medium":"https://randomuser.me/api/portraits/med/women/48.jpg","thumbnail":"https://randomuser.me/api/portraits/thumb/women/48.jpg"}},
{"gender":"female","name":{"title":"mrs","first":"leta","last":"hale"},"location":{"street":"1060 cackson st","city":"fontana","state":"ohio","postcode":96886},"dob":"1971-11-27 16:42:44","id":{"name":"SSN","value":"321-92-8250"},"picture":{"large":"https://randomuser.me/api/portraits/women/46.jpg","medium":"https://randomuser.me/api/portraits/med/women/46.jpg","thumbnail":"https://randomuser.me/api/portraits/thumb/women/46.jpg"}},
{"gender":"male","name":{"title":"mr","first":"paul","last":"payne"},"location":{"street":"8297 sunset st","city":"amarillo","state":"illinois","postcode":58451},"dob":"1978-04-02 07:23:24","id":{"name":"SSN","value":"803-15-9208"},"picture":{"large":"https://randomuser.me/api/portraits/men/18.jpg","medium":"https://randomuser.me/api/portraits/med/men/18.jpg","thumbnail":"https://randomuser.me/api/portraits/thumb/men/18.jpg"}}
]

print("\nThe length of the list is: " + str(len(data)) )

print("\nHere's one person's data:\n")
print(data[0])

print("\nHere's one person's name data only:\n")
print(data[0]['name'])

print("\nHere's one person's location data only:\n")
print(data[0]['location'])

print("\nHere's one person's city data only:\n")
print(data[0]['location']['city'])

print("\nNow we'll run a loop to get each person's first and last name:\n")
for person in data:
    print(person['name']['first'] + " " + person['name']['last'])

print("\nAnd another loop to get each person's ID number, gender, \ncity, and date of birth:\n")
for person in data:
    print(person['id']['value'])
    print(person['gender'])
    print(person['location']['city'])
    print(person['dob'])
    print("\n")
