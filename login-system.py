print('Create account now')
username = input('Enter username: ')
password = input('Enter Password: ')

print('Your account has been created successfully')
print('login now!')

username2 = input('Enter username: ')
password2 = input('Enter password: ')

if username == username2 and password == password2:
    print('Logged in succesfully')
else:
    print('Invalid credentials')