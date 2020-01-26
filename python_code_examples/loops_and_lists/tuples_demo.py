# a list uses square brackets
# a tuple uses parentheses
cars_list = ('Ford', 'Honda', 'Volkswagen', 'Chevy', 'Dodge', 'Hyundai')

# demo shows that list methods do not work on a tuple, which is immutable

try:
    cars_list.remove('Volkswagen')
except AttributeError as err:
    print(err)

try:
    cars_list.append('BMW')
except AttributeError as err:
    print(err)

# note, this works fine - we can access any tuple item with its index
print(cars_list[1] + " and " + cars_list[2])

try:
    cars_list.insert(1, 'BMW')
except AttributeError as err:
    print(err)

try:
    cars_list.sort()
except AttributeError as err:
    print(err)

try:
    cars_list.reverse()
except AttributeError as err:
    print(err)

# we can loop over a tuple just like a list
for car in cars_list:
    print(car)

for index, item in enumerate(cars_list):
    print('The index: ' + str(index) + ' The item: ' + item)
