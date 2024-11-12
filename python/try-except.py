try:
    x = int(input('Input an integer: '))
    print(x)
except:
    print('Something went wrong')
finally:
    print('try except finished')