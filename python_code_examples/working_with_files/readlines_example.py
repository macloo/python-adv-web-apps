# open a file for reading
states = open('state_data.txt')
# open a new file for writing
capitals = open('capitals.txt', 'w')
# store the result of readlines() in a variable
states_list = states.readlines()
# loop over the list that resulted from readlines()
for state in states_list:
    foo = state.split('\t')               # split the line at the tabs
    text = foo[1] + ", " + foo[0] + '\n'  # create text: capital, state
    capitals.write(text)                  # write text into the new file
# close both files
capitals.close()
states.close()
