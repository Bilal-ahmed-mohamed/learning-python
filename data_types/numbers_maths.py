#############################################################
# Python Numbers, Type Conversion and Mathematics
#############################################################

# The number data types are used to store the numeric values.


# int - holds signed integers of non-limited length.
# float - holds floating decimal points and it's accurate up to 15 decimal places.
# complex - holds complex numbers.

num1 = 5
print(num1, 'is of type', type(num1))

num2 = 5.42
print(num2, 'is of type', type(num2))

num3 = 8+2j
print(num3, 'is of type', type(num3))


# Python offers the random module to generate random numbers or to pick a random item from an iterator.

import random

print(random.randrange(20, 30))

list1 = ['a', 'b', 'c', 'd', 'e']

# get random item from list1
print(random.choice(list1))

# Shuffle list1
random.shuffle(list1)

# Print the shuffled list1
print(list1)

# Print random element
print(random.random())