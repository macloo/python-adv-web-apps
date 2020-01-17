'''
    How to construct a conditional sequence with if-elif-else:

    must start with an if statement
    must have only ONE if statement
    may have as many elif statements as needed - or none
    may have one else statement - or none
    must not have more than one else statement
'''

print("What is your name?")
name = input()
print("How old are you?")
age = input()

if name == 'Alice' and int(age) < 13:
    print("How's Wonderland?")
elif name == 'Alice':
    print("You are too old to enter through the looking glass.")
elif int(age) < 13:
    print('You are not yet a teen.')
else:
    print('You are neither Alice nor a little kid.')
