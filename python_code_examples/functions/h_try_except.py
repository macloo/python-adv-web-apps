# error handling: use this try/except pattern

def test_for_int(num):

    try:
        num = int(num)
        message = str(num) + " is an integer. Good job!"

    # this exception handles any entry that was NOT an integer
    except ValueError:
        message = "Error: You did not provide a whole number."

    return message

# ask for user input
response = input("Enter a number: ")

# run the function, and print what is returned
print( test_for_int(response) )
