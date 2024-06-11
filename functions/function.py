

# A function is a block of code that performs a specific task

    

# def greet():
#     print('Hello bilal')


# greet()



#############################################
# Python Function Arguments
#############################################

def greet(name):
    print("Hello", name)


greet("bilal")


############################################
# Example: Function to Add Two Numbers
############################################

# function with two arguments
def add_numbers(num1, num2):
    sum = num1 + num2
    print("Sum: ", sum)


add_numbers(5, 4)


##########################
# The return Statement
#########################

def findSquare(num):
    result = num * num
    return result

square = findSquare(11)
print("square :" , square)



#########################
# The pass Statement
##########################

# The pass statement serves as a placeholder for future code, preventing errors from empty code blocks.
# It's typically used where code is planned but has yet to be written.

def future_function():
    pass

# this will execute without any action or error
future_function()  



import math

# sqrt computes the square root
square_root = math.sqrt(4)

print("Square Root of 4 is",square_root)


power = pow(2, 3)

print("2 to the power 3 is",power)



##################################
# Python Function Arguments
####################################

# In computer programming, an argument is a value that is accepted by a function.

def add_numbers(a, b):
    sum = a + b
    print('Sum:', sum)

add_numbers(2, 3)

# Function Argument with Default Values
# In Python, we can provide default values to function arguments.
# We use the = operator to provide default values. 

def add_numbers( a = 7,  b = 8):
    sum = a + b
    print('Sum:', sum)


# function call with two arguments
add_numbers(2, 3)

#  function call with one argument
add_numbers(a = 2)

# function call with no arguments
add_numbers()



# Python Keyword Argument
# In keyword arguments, arguments are assigned based on the name of the arguments.
def display_info(first_name, last_name):
    print('First Name:', first_name)
    print('Last Name:', last_name)

display_info(last_name = 'Cartman', first_name = 'Eric')



# Python Function With Arbitrary Arguments

# Sometimes, we do not know in advance the number of arguments that will be passed into a function. To handle this kind of situation, we can use arbitrary arguments in Python.

# program to find sum of multiple numbers 
# Arbitrary arguments allow us to pass a varying number of values during a function call.
#  We use an asterisk (*) before the parameter name to denote this kind of argument. For example,

def find_sum(*numbers):
    result = 0
    
    for num in numbers:
        result = result + num
    
    print("Sum = ", result)

find_sum(1, 2, 3)


find_sum(4, 9)

find_sum(10,20,30)


##################################
# Python Variable Scope
##################################

# In Python, we can declare variables in three different scopes: local scope, global, and nonlocal scope.

# 1.Python Local Variables
# When we declare variables inside a function, these variables will have a local scope (within the function). We cannot access them outside the function.


def greet():

    # local variable
    message = 'Hello'
    print(message)
    print('Local', message)

greet()

# 2.Python Global Variables
# In Python, a variable declared outside of the function or in global scope is known as a global variable. This means that a global variable can be accessed inside or outside of the function.

# declare global variable
message = 'Hello'

def greet():
    # declare local variable
    print('Local', message)

greet()
print('Global', message)

# 3.Python Nonlocal Variables
# In Python, nonlocal variables are used in nested functions whose local scope is not defined. This means that the variable can be neither in the local nor the global scope.

# We use the nonlocal keyword to create nonlocal variables.

# outside function 
def outer():
    message = 'local'

    # nested function  
    def inner():

        # declare nonlocal variable
        nonlocal message

        message = 'nonlocal'
        print("inner:", message)

    inner()
    print("outer:", message)

outer()


######################################################
# Python Global Keyword
######################################################

# In Python, the global keyword allows us to modify the variable outside of the current scope.
# It is used to create a global variable and make changes to the variable in a local context.

# Access and Modify Python Global Variable
c = 1 

def add():
    print(c)

add()

# Changing Global Variable From Inside a Function using global

# global variable
c = 1 

def add():

    # use of global keyword
    global c

    # increment c by 2
    c = c + 2 

    print(c)

add()

# Global in Nested Functions

# In Python, we can also use the global keyword in a nested function.
def outer_function():
    num = 20

    def inner_function():
        global num
        num = 25
    
    print("Before calling inner_function(): ", num)
    inner_function()
    print("After calling inner_function(): ", num)

outer_function()
print("Outside both function: ", num)

########################## Rules of global Keyword#####################
# 1.When we create a variable inside a function, it is local by default
# 2.When we define a variable outside of a function, it is global by default. You don't have to use the global keyword.
# 3.We use the global keyword to read and write a global variable inside a function.
# 4.Use of the global keyword outside a function has no effect.



                ################################################################
                                 # Python Recursion
                ###############################################################                 



# Recursion is the process of defining something in terms of itself.

# Python Recursive Function
# In Python, we know that a function can call other functions. It is even possible for the function to call itself. These types of construct are termed as recursive functions.

# Example of a recursive function
def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


num = 3
print("The factorial of", num, "is", factorial(num))

# Our recursion ends when the number reduces to 1. This is called the base condition.
# The Python interpreter limits the depths of recursion to help avoid infinite recursions, resulting in stack overflows.

# Advantages of Recursion
# 1.Recursive functions make the code look clean and elegant.
# 2.A complex task can be broken down into simpler sub-problems using recursion.
# 3.Sequence generation is easier with recursion than using some nested iteration.


# Disadvantages of Recursion
# 1.Sometimes the logic behind recursion is hard to follow through.
# 2.Recursive calls are expensive (inefficient) as they take up a lot of memory and time.
#3. Recursive functions are hard to debug.



                    ################################################################
                                     # Python Modules
                    ###############################################################  

# As our program grows bigger, it may contain many lines of code. Instead of putting everything in a single file, we can use modules to separate codes in separate files as per their functionality. This makes our code organized and easier to maintain.

# Import Python Standard Library Modules
# The Python standard library contains well over 200 modules. We can import a module according to our needs.

# The dir() built-in function
# In Python, we can use the dir() function to list all the function names in a module.

# For example, earlier we have defined a function add() in the module

# dir(example)

# ['__builtins__',
# '__cached__',
# '__doc__',
# '__file__',
# '__initializing__',
# '__loader__',
# '__name__',
# '__package__',
# 'add']



                ##################################################################
                                     # Python Package
                ###################################################################

# A package is a container that contains various functions to perform specific tasks. For example, the math package includes the sqrt() function to perform the square root of a number.

# While working on big projects, we have to deal with a large amount of code, and writing everything together in the same file will make our code look messy. Instead, we can separate our code into multiple files by keeping the related code together in packages.

# Now, we can use the package whenever we need it in our projects. This way we can also reuse our code.



# Note: A directory must contain a file named __init__.py in order for Python to consider it as a package. This file can be left empty but we generally place the initialization code for that package in this file.




# Importing module from a package


# In Python, we can import modules from packages using the dot (.) operator.

# For example, if we want to import the start module in the above example, it can be done as follows:

# import Game.Level.start

# Now, if this module contains a function named select_difficulty(), we must use the full name to reference it.
# Game.Level.start.select_difficulty(2)

# Import Without Package Prefix
# If this construct seems lengthy, we can import the module without the package prefix as follows:
# from Game.Level import start

# We can now call the function simply as follows:
# start.select_difficulty(2)

# Import Required Functionality Only
# Another way of importing just the required function (or class or variable) from a module within a package would be as follows:
# from Game.Level.start import select_difficulty

# Now we can directly call this function.
# select_difficulty(2)

# Although easier, this method is not recommended. Using the full namespace avoids confusion and prevents two same identifier names from colliding.

# While importing packages, Python looks in the list of directories defined in sys.path, similar as for module search path.



            #############################################################################
                                    # Python Main function
            ##############################################################################

# What is the main() function in Python?
# Some programming languages have a special function called main() which is the execution point for a program file. Python interpreter, however, runs each line serially from the top of the file and has no explicit main() function.

# Python offers other conventions to define the execution point. One of them is using the main() function and the __name__ property of a python file.

# The __name__ variable is a special builtin Python variable that shows the name of the current module.

# It has different values depending on where we execute the Python file. Let's look at an example.


# Running Python File as a Script
# Suppose we have a Python file called helloworld.py with the following content:
# print(__name__)

# If we run helloworld.py from the command line, then it runs as a Python script. We can run the Python program using the following command:

# $ python helloworld.py

# When we run the program as a script, the value of the variable __name__ is set to __main__. So the output of the following program will be:

# __main__



# Running Python file as a Module
# We can also run a Python file as a module. For this, we have to import this file into another Python program. Let's look at an example.

# Suppose we have a Python file called main.py in the same directory as the heloworld.py file. It has the following content:

# import helloworld
# When we run this file, we will have the following output:
# helloworld
# Here, we can see that importing a module also runs all the code in the module file.
# But, we can see that instead of displaying __main__, the program displays the name of the module i.e. helloworld.
# It is because, in the context of running a Python file as a module, the name of the module itself is assigned to the __name__ variable.

# Using if conditional with __name__
# Now that we have understood how __name__ variable is assigned values, we can use the if conditional clause to run the same Python file differently in different contexts.

# Let's look at an example.

# Suppose we change the content of the helloworld.py file to the following:

# def main():
#     print("Hello World")

# if __name__=="__main__":
#     main()
# Now, when we run it as a script via the command line, the output will be:
# Hello World

# However, when we run it as a module by importing it in the main.py file, no output is displayed since the main() function is not called.

# Here, we have created a custom main() function in the helloworld.py file. It is executed only when the program is run as a standalone script and not as an imported module.

# This is the standard way to explicitly define the main() function in Python. It is one of the most popular use cases of __name__ variable of a Python file.