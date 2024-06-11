# Python List
# In Python, lists allow us to store a sequence of items in a single variable.

ages = [20,30,50]
print(ages)

student = ['bilal' , 32 , 'cs']
print(student)
print(student[0])

empty_list = []
print(empty_list)


# Lists are:

# Ordered - They maintain the order of elements.
# Mutable - Items can be changed after creation.
# Allow duplicates - They can contain duplicate values.


my_list = ['p', 'r', 'o', 'g', 'r', 'a', 'm']

# items from index 2 to index 4
print(my_list[2:5])

# items from index 5 to end
print(my_list[5:])

# items beginning to end
print(my_list[:])

# We use the append() method to add an element to the end of a Python list
# We can change the items of a list by assigning new values using the = operator. 
colors = ['Red', 'Black', 'Green']
print('Original List:', colors)

# changing the third item to 'Blue'
colors[2] = 'Blue'

print('Updated List:', colors)
# We can remove an item from a list using the remove() method. For example,
numbers = [2,4,7,9]

# remove 4 from the list
numbers.remove(4)

print(numbers) 

# Output: [2, 7, 9]


# We can use the built-in len() function to find the number of elements in a list.
cars = ['BMW', 'Mercedes', 'Tesla']

print('Total Elements: ', len(cars))  
  

##################################################
# Iterating Through a List
#################################################

fruits = ['apple', 'banana', 'orange']



fruits.append('melon')
fruits.extend('watermelon')    
fruits.count(fruits)

for fruit in fruits:
    print(fruit)
