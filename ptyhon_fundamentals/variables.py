# numbers

number = 22
print(number)

# string
lapy_name = 'lapy_wzmu'
print(lapy_name)

# Assigning multiple values to multiple variables
a , b , c= 20 , 4.5 , 'bilal'
print(a)
print(b)
print(c)

# If we want to assign the same value to multiple variables at once, we can do this as:
plan1 = plan2 = 'sleeping'
print(plan2)
print(plan1)

# ##################################
# Python Type Conversion
# ###################################

# 1.Implicit Conversion - automatic type conversion
# In certain situations, Python automatically converts one data type to another. This is known as implicit type conversion.

integer_number = 123
float_number = 1.23

new_number = integer_number + float_number

# display new value and resulting data type
print("Value:",new_number)
print("Data Type:",type(new_number))

# 2.Explicit Type Conversion
# In Explicit Type Conversion, users convert the data type of an object to required data type.
# We use the built-in functions like int(), float(), str(), etc to perform explicit type conversion.
# This type of conversion is also called typecasting because the user casts (changes) the data type of the objects.

num_string = '12'
num_integer = 23

print("Data type of num_string before Type Casting:",type(num_string))

# explicit type conversion
num_string = int(num_string)

print("Data type of num_string after Type Casting:",type(num_string))

num_sum = num_integer + num_string

print("Sum:",num_sum)
print("Data type of num_sum:",type(num_sum))


############################################################
# Python Basic Input and Output
############################################################

# In Python, we can simply use the print() function to print output. For example,

# Syntax of print()
# In the above code, the print() function is taking a single parameter.
# However, the actual syntax of the print function accepts 5 parameters

# print(object= separator= end= file= flush=)
# Here,

# object - value(s) to be printed
# sep (optional) - allows us to separate multiple objects inside print().
# end (optional) - allows us to add add specific values like new line "\n", tab "\t"
# file (optional) - where the values are printed. It's default value is sys.stdout (screen)
# flush (optional) - boolean specifying if the output is flushed or buffered. Default: False


# python print() with end Parameter
# print with end whitespace
print('Good Morning!', end= ' ')

print('It is rainy today')
# Python print() with sep parameter
print('New Year', 2023, 'See you soon!', sep= '. ')

# Print Concatenated Strings
# We can also join two strings together inside the print() statement. For example,
print('am coding in python ' + 'imagine.')

# Output formatting
# Sometimes we would like to format our output to make it look attractive. This can be done by using the str.format() method. For example,
x = 5
y = 10

print('The value of x is {} and y is {}'.format(x,y))


# using input() to take user input
num = input('Enter a number: ')

print('You Entered:', num)

print('Data type of num:', type(num))



##############################################################
# Python Operators
################################################################
# Arithmetic Operators
# Assignment Operators
# Comparison Operators
# Logical Operators
# Bitwise Operators
# Special Operators


message = 'Hello world'
dict1 = {1:'a', 2:'b'}

# check if 'H' is present in message string
print('H' in message)  # prints True

# check if 'hello' is present in message string
print('hello' not in message)  # prints True

# check if '1' key is present in dict1
print(1 in dict1)  # prints True

# check if 'a' key is present in dict1
print('a' in dict1)  # prints False