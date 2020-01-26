# this file demos three ways to loop over a list
# same list, three ways

fruit_list = ['mango', 'apple', 'pear', 'banana', 'pomegranate']

print("\nFirst loop (for fruit in ...):\n")

for fruit in fruit_list:
    print(fruit)

print("\nSecond loop (range):\n")

for i in range( len(fruit_list) ):
    print( str(i + 1) + ". " + fruit_list[i] )

print("\nThird loop (enumerate):\n")

for index, item in enumerate(fruit_list):
    print('The index: ' + str(index) + ' The item: ' + item)

print() # blank line
