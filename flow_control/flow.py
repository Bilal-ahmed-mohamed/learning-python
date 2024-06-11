# Python if Statement


age = 25

if age > 0:
    print('you can drive')



 # Python if...else Statement

number = -5

if number > 0:
    print("positive number")
else:
    print("negative number")


# Python if…elif…else Statement

money = 0

if money > 0:
    print("+tve number")
elif money < 0:
    print("-tve number")
else:
    print("zero")

# Python Nested if Statements
number = 5

# outer if statement
if number >= 0:
    # inner if statement
    if number == 0:
      print('Number is 0')
    
    # inner else statement
    else:
        print('Number is positive')

# outer else statement
else:
    print('Number is negative')
