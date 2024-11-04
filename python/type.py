value = input('Input a value: ')

if type(value) == str:
    print(value + ' is a string')
elif type(value) == int:
    print(value + ' is a integer')
elif type(value) == list:
    print(value + ' is a list')
else:
    print('we dont\'t know the data type of' + value)
