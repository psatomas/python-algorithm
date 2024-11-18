num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
op = input('Enter Operator')

if op == '+':
    print('The addition is', num1 + num2)
elif op == '-':
    print('The subtraction is', num1 - num2)
elif op == '*':
    print('The multiplication is', num1 * num2)
elif op == '/':
    print('The division is', abs(num1 / num2))
else:
    print('Invalid operator')