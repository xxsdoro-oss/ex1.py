username = input('Enter a username:')


if len(username) > 12:
    print('Your user name can\'t be more than 12 characters.')
elif username.find(' ') == -1:
    print('Your username can\'t contain spaces.')
elif username.isalpha():
    print('Your username can\'t contain numbers.')
else:
    print(f'Welcome {username} !')
