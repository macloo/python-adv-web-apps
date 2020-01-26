import pathlib

def create_file():
    """create a new file after first making sure the filename does not
       already exist in the current working directory
    """
    proposed_filename = input("\nWhat filename would you like? ")

    while True:
        path = pathlib.Path(proposed_filename)
        # check for a previously existing file with that name
        if ( path.exists() ):
            print("\nThat filename already exists.")
            # ask user for a new filename
            proposed_filename = input("\nWhat should the filename be? ")
        else:
            newfile = open(proposed_filename, 'w')
            newfile.close()
            print("\nThe file " + proposed_filename + " has been created.\n")
            # quit the while-loop
            break

# call the function
create_file()
