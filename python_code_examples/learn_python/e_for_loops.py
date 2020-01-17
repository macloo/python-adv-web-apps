import random

# these 4 for-loops all use range()
# note, for-loops can be used on Python lists without range()
# range takes 1, 2, or 3 arguments

# for-loop No. 1
print('1. We will multiply by 8, five times:')
for i in range(1,6):
    i = i * 8
    print(i)

print() # blank line

# for-loop No. 2
print('2. We will print "foobar" 3 times:')
for i in range(3):
    print('foobar')

print() # blank line

# for-loop No. 3
num = random.randint(2, 15)
print('3. We will print a random number that number of times:')
for i in range(num):
    print(num)

print() # blank line

# for-loop No. 4
print('4. We will use the step option to count by fives:')
for i in range(0, 40, 5):
    print(i)

print() # blank line
