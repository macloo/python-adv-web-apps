# note that making the conditional True (as here) may
# sometimes cause an infinite loop
# press Control-C to get out of an infinite loop 

while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        # return to the top of the loop
        continue
    print('Hello, Joe. What is the password?')
    password = input()
    if password == 'swordfish':
        # quit the loop
        break
    else:
        print('That is not correct, Joe.')
        # return to the top of the loop
        continue

print('Access granted.')
