import pprint
pp = pprint.PrettyPrinter(indent=4)

# below is a Python dictionary - note how it differs in structure from
# a Python list - a dictionary stores key-value PAIRS
cat = { 'eyes': 'green',
    'fur': 'brown',
    'name': 'Furball',
    'nose': 'pink',
    'tail': 'short' }

# add a new item to the dictionary
cat.update({'ears':'pointy'})

# change an item in the dictionary - same as adding a new item
cat.update({'fur':'orange'})

print("\n")

print(cat)

print("\n")

# we imported pprint (not normally needed for dictionaries)
# so we could see this difference in printing in Terminal
pp.pprint(cat)

print("\n")

print('Print the value of "nose":')
print(cat['nose'])

print("\n")

print('Print the value of "name":')
print(cat['name'])

print("\n")

print("The cat's name is " + cat['name'] + " and the cat's nose is " + cat['nose'] + ".")

print("\n")

new_name = input("Give the cat a new name: ")

cat.update({'name':new_name})

print("The cat's name is now " + cat['name'] + ".")

print("\n")
