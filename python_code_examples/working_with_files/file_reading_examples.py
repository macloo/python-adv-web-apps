# this program demonstrates some ways to read a file
# and print its contents to the Terminal
# it only reads - it does not write 

# create new file object using a file containing text
myfile = open('jabberwocky.txt')

print("\nWe have opened a file that contains an eight-line poem.\n")
print("\nWe'll create a list with readlines() ...\n")

# create a list in which each item is one line from the file
line_list = myfile.readlines()

print("\nThis is the Python list that was created from the file:\n")

# print the entire list
print(line_list)

input("\n\nPress any key to continue ...\n")

print("\nWe will loop through the items in that list:\n\n")

# loop line by line
for line in line_list:
    print(line)

input("\nPress any key to continue ...\n")

print("\nNow let's STRIP the newlines and leading spaces from \
    \nthe items as we loop through the list:\n")

# loop line by line, and strip each line before printing
for line in line_list:
    print( line.strip() )

input("\n\nPress any key to continue ...")

print("\nLet's print the contents of the file:\n")

# print contents of entire file (attempt)
print( myfile.read() )

print("\nNothing happened, because we were at the END of the file.\n")

# return to start of file
myfile.seek(0)

print("\nLet's try again to print the contents of the file:\n")

# print contents of entire file
print( myfile.read() )

# close the file
myfile.close()
