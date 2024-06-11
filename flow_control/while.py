#########################
# Python while Loop
########################

# In Python, we use the while loop to repeat a block of code until a certain condition is met.

number = 1

while number <= 5:
    print(number)
    number = number + 1


##################################################
 # Calculate the sum of numbers until user enters 0
 ##################################################

age = int(input("Enter Age:"))

total = 0

# continue until the user enters age as 0
while age != 0:
    total += age
    age = int(input("Enter Age:"))

    print('The sum is', total)


age = 32

