# 1. Write a function named right_justify that takes a string named s as a parameter
# and prints the string with enough leading spaces so that the last letter of the string is in column 70
# of the display.
# >>> right_justify('monty')
# monty
# Hint: Use string concatenation and repetition. Also, Python provides a built-in function called len
# that returns the length of a string, so the value of len('monty') is 5.

def right_justify(s):
    total_width = 70
    leading_spaces = total_width - len(s)
    print(' ' * leading_spaces + s)

right_justify('monty')

# 2. A function object is a value you can assign to a variable or pass as an argument. For
# example, do_twice is a function that takes a function object as an argument and calls it twice:
# def do_twice(f):
# f()
# f()
# Here’s an example that uses do_twice to call a function named print_spam twice.
# def print_spam():
# print('spam')
# do_twice(print_spam)
# 1. Type this example into a script and test it.
# 2. Modify do_twice so that it takes two arguments, a function object and a value, and calls the
# function twice, passing the value as an argument.
# 3. Copy the definition of print_twice from earlier in this chapter to your script.
# 4. Use the modified version of do_twice to call print_twice twice, passing 'spam' as an
# argument.
# 5. Define a new function called do_four that takes a function object and a value and calls the
# function four times, passing the value as a parameter. There should be only two statements in
# the body of this function, not four.

# 1. Original example
def do_twice(f):
    f()
    f()

def print_spam():
    print('spam')

do_twice(print_spam)


# 2. Modified do_twice: now takes a function AND a value
def do_twice(f, value):
    f(value)
    f(value)


# 3. print_twice from earlier in the chapter
def print_twice(text):
    print(text)
    print(text)


# 4. Use modified do_twice to call print_twice twice
do_twice(print_twice, 'spam')


# 5. Define do_four using only TWO statements inside the function
def do_four(f, value):
    do_twice(f, value)
    do_twice(f, value)


# Test do_four
do_four(print_twice, 'spam')

# 3. Note: This exercise should be done using only the statements and other features we
# have learned so far.
# 1. Write a function that draws a grid like the following:
#"grid not avaible"
# Hint: to print more than one value on a line, you can print a comma-separated sequence of
# values:
# print('+', '-')
# By default, print advances to the next line, but you can override that behavior and put a
# space at the end, like this:
# print('+', end=' ')
# print('-'
# The output of these statements is '+ -' on the same line. The output from the next print
# statement would begin on the next line.
# 2. Write a function that draws a similar grid with four rows and four columns.

# 1. two rows and two columns
def print_horizontal():
    print('+ - - - - + - - - - +')

def print_vertical():
    print('|         |         |')

def print_grid():
    print_horizontal()
    for i in range(4):
        print_vertical()
    print_horizontal()
    for i in range(4):
        print_vertical()
    print_horizontal()

print_grid()

# 2. two rows and two columns
def print_horizontal():
    print('+ - - - - + - - - - + - - - - + - - - - +')

def print_vertical():
    print('|         |         |         |         |')

def print_grid():
    print_horizontal()
    for i in range(4):
        print_vertical()
    print_horizontal()
    for i in range(4):
        print_vertical()
    print_horizontal()
    for i in range(4):
        print_vertical()
    print_horizontal()
    for i in range(4):
        print_vertical()
    print_horizontal()

print_grid()