print("What is your name?")
name = input()
print("How old are you?")
age = input()

if name == 'Alice' and int(age) < 13:
    print("How's Wonderland?")
elif name == 'Alice':
    print("You are too old to enter through the looking glass, Alice.")
elif int(age) < 13:
    print('This is only for Alice, kiddo.')
else:
    print('You are not Alice, and you are 13 or older.')
