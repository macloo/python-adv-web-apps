'''
    An interactive demo of a while-loop.
    Depending on what you type when prompted, the loop
    will either continue or quit.
'''

word = "spam"

while word == "spam":
    print("Spam spam spam spam")
    print("Type the word spam.")
    word = input()

print("No more spam 😥")
