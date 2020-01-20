# error handling: use this try/except pattern
# to find out what kind of error would be thrown, experiment at
# the Python command line (error types are case sensitive)

def test_for_int(num):

    try:
        num = int(num)
        message = str(num) + " is an integer. Good job!"
    # this exception handles any entry that was NOT an integer
    except ValueError:
        message = "Error: You did not provide a whole number."

    return message

# ask for user input on the same line 
response = input("Enter a number: ")

# run the function, and print what is returned
print( test_for_int(response) )
