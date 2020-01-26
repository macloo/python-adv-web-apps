cars_list = ['Ford', 'Honda', 'Volkswagen', 'Chevy', 'Dodge', 'Hyundai']

def deplete_list(list_name):
    """remove all items from a list"""

    while len(list_name) > 0:
        # remove last item from list, store it in a variable
        item = list_name.pop()
        print(item + " was removed ...")
        print("Now there are " + str( len(list_name) ) + " items in the list.")

    print("There are no items left in the list.")

# call the function
deplete_list(cars_list)

print(cars_list)
