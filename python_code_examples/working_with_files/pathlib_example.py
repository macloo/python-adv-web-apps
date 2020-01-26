import pathlib

print("\nThe current directory is:")
print( pathlib.Path.cwd() )
print() # blank line

def check_for_filename(filename):
    """find out whether a file already exists in the current working
       directory
    """
    # create Path for filename of a new file
    path = pathlib.Path.cwd() / filename

    # check whether filename already exists
    if path.exists():
        print("The filename " + filename + " is already in use.")
    else:
        print("There is no file named " + filename + ".")

    print() # blank line

# call the function twice
check_for_filename("foobar.txt")
check_for_filename("jabberwocky.txt")
