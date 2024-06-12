
###################################################################################################
                        # Python Exceptions
####################################################################################################


# An exception is an unexpected event that occurs during program execution. For example,

##################       Python Logical Errors (Exceptions)  #########################

# Errors that occur at runtime (after passing the syntax test) are called exceptions or logical errors.

# For instance, they occur when we

# try to open a file(for reading) that does not exist (FileNotFoundError)
# try to divide a number by zero (ZeroDivisionError)
# try to import a module that does not exist (ImportError) and so on.

# Whenever these types of runtime errors occur, Python creates an exception object.

# If not handled properly, it prints a traceback to that error along with some details about why that error occurred.

# e.g
divide_numbers = 7 / 0
print(divide_numbers)


################################   Python Built-in Exceptions #################################

# Illegal operations can raise exceptions. There are plenty of built-in exceptions in Python that are raised when corresponding errors occur.
# We can view all the built-in exceptions using the built-in local() function as follows:


print(dir(locals()['__builtins__']))

# Here, locals()['__builtins__'] will return a module of built-in exceptions, functions, and attributes and dir allows us to list these attributes as strings.

# We can handle these built-in and user-defined exceptions in Python using try, except and finally statements. To learn more about them, visit Python try, except and finally statements.

# Python Error and Exception

# Errors represent conditions such as compilation error, syntax error, error in the logical part of the code, library incompatibility, infinite recursion, etc.
# Errors are usually beyond the control of the programmer and we should not try to handle errors.
# Exceptions can be caught and handled by the program.


#############################################################################################################
                                    # Python Exception Handling
#############################################################################################################

# Since exceptions abnormally terminate the execution of a program, it is important to handle exceptions. In Python, we use the try...except block to handle exceptions.


############################    Python try...except Block ###########################

# The try...except block is used to handle exceptions in Python. Here's the syntax of try...except block:

# try:
#     # code that may cause exception
# except:
#     # code to run when exception occurs

# Here, we have placed the code that might generate an exception inside the try block. Every try block is followed by an except block.
#  When an exception occurs, it is caught by the except block. The except block cannot be used without the try block.


#    Example: Exception Handling Using try...except

try:
    numerator = 10
    denominator = 0

    result = numerator/denominator

    print(result)
except:
    print("Error: Denominator cannot be 0.")

# To handle the exception, we have put the code, result = numerator/denominator inside the try block. Now when an exception occurs, the rest of the code inside the try block is skipped.
# The except block catches the exception and statements inside the except block are executed.
# If none of the statements in the try block generates an exception, the except block is skipped.


###############################   Catching Specific Exceptions in Python ##########################

# For each try block, there can be zero or more except blocks. Multiple except blocks allow us to handle each exception differently.
# The argument type of each except block indicates the type of exception that can be handled by it. For example,

try:
    
    even_numbers = [2,4,6,8]
    print(even_numbers[5])

except ZeroDivisionError:
    print("Denominator cannot be 0.")
    
except IndexError:
    print("Index Out of Bound.")

# In this example, we have created a list named even_numbers.

# Since the list index starts from 0, the last element of the list is at index 3. Notice the statement,

print(even_numbers[5])
# Here, we are trying to access a value to the index 5. Hence, IndexError exception occurs.

# When the IndexError exception occurs in the try block,

# The ZeroDivisionError exception is skipped.
# The set of code inside the IndexError exception is executed.

#########################################   Python try with else clause ############################

# In some situations, we might want to run a certain block of code if the code block inside try runs without any errors.
# For these cases, you can use the optional else keyword with the try statement.

# Let's look at an example:

# program to print the reciprocal of even numbers

try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0
except:
    print("Not an even number!")
else:
    reciprocal = 1/num
    print(reciprocal)

#  Here, the assert statement in the code checks that num is an even number; if num is odd, it raises an AssertionError, triggering the except block.
# Note: Exceptions in the else clause are not handled by the preceding except clauses.

####################################   Python try...finally #######################

# In Python, the finally block is always executed no matter whether there is an exception or not.
# The finally block is optional. And, for each try block, there can be only one finally block.

try:
    numerator = 10
    denominator = 0

    result = numerator/denominator

    print(result)
except:
    print("Error: Denominator cannot be 0.")
    
finally:
    print("This is finally block.")


# In the above example, we are dividing a number by 0 inside the try block. Here, this code generates an exception.
# The exception is caught by the except block. And, then the finally block is executed.


############################################################################################################################
                                # Python Custom Exceptions
###########################################################################################################################

# However, sometimes we may need to create our own custom exceptions that serve our purpose.


#################  Defining Custom Exceptions ##################

# In Python, we can define custom exceptions by creating a new class that is derived from the built-in Exception class.
# Here's the syntax to define custom exceptions,

class CustomError(Exception):
    ...
    pass

try:
   ...

except CustomError:
    ...

# Here, CustomError is a user-defined error which inherits from the Exception class.

# Note:

# When we are developing a large Python program, it is a good practice to place all the user-defined exceptions that our program raises in a separate file.
# Many standard modules define their exceptions separately as exceptions.py or errors.py (generally but not always).    



###########################    Example: Python User-Defined Exception ##########

# define Python user-defined exceptions
class InvalidAgeException(Exception):
    "Raised when the input value is less than 18"
    pass

# you need to guess this number
number = 18

try:
    input_num = int(input("Enter a number: "))
    if input_num < number:
        raise InvalidAgeException
    else:
        print("Eligible to Vote")
        
except InvalidAgeException:
    print("Exception occurred: Invalid Age")

# Here, when input_num is smaller than 18, this code generates an exception.
# When an exception occurs, the rest of the code inside the try block is skipped.
# The except block catches the user-defined InvalidAgeException exception and statements inside the except block are executed.

################################    Customizing Exception Classes #######################

# We can further customize this class to accept other arguments as per our needs.
# To learn about customizing the Exception classes, you need to have the basic knowledge of Object-Oriented programming.
# Visit Python Object Oriented Programming to learn about Object-Oriented programming in Python.

class SalaryNotInRangeError(Exception):
    """Exception raised for errors in the input salary.

    Attributes:
        salary -- input salary which caused the error
        message -- explanation of the error
    """

    def __init__(self, salary, message="Salary is not in (5000, 15000) range"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)


salary = int(input("Enter salary amount: "))
if not 5000 < salary < 15000:
    raise SalaryNotInRangeError(salary)

# Here, we have overridden the constructor of the Exception class to accept our own custom arguments salary and message.
# Then, the constructor of the parent Exception class is called manually with the self.message argument using super().
# The custom self.salary attribute is defined to be used later.
# The inherited __str__ method of the Exception class is then used to display the corresponding message when SalaryNotInRangeError is raised.