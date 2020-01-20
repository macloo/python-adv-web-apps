# a simple example of a "black box" function
# put in two words, and a string is returned
# a and b are parameters
# "love" and "Gators" are the arguments passed to the function
# the value of result is returned

def add_things(a, b):
    result = (a * 3) + (b * 3)
    return result

# the data returned by the function is stored in a new variable, output
output = add_things("love", "Gators")

# we can print the value of output, or we could send it to a database, etc.
print(output)
