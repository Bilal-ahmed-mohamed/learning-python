##########################################
# Python Sets
############################################


# A set is a collection of unique data, meaning that elements within a set cannot be duplicated.

# For instance, if we need to store information about student IDs, a set is suitable since student IDs cannot have duplicates.

# In Python, we create sets by placing all the elements inside curly braces {}, separated by commas

# A set can have any number of items and they may be of different types (integer, float, tuple, string, etc.). But a set cannot have mutable elements like lists, sets or dictionaries as its elements.


student_id = {112, 114, 116, 118, 115}
print('Student ID:', student_id)

mixed_set = {'Hello', 101, -2, 'Bye'}
print('Set of mixed data types:', mixed_set)

# Here, we can see there are no duplicate items in the set as a set cannot contain duplicates.


########################################
# Add and Update Set Items in Python
###########################################

numbers  = {23,45,67,89}
print('initial set:' , numbers)

numbers.add(34)
print('updated set:' , numbers)

###########################################
# Update Python Set
###########################################

companies = {'Lacoste', 'Ralph Lauren'}
tech_companies = ['apple', 'google', 'apple']
companies.update(tech_companies)
print(companies)
print(tech_companies)

removedValue = companies.discard('apple')
print('Set after remove():', companies)



                         ##################################################################
                                # Python Set Operations
                        ###################################################################

# Python Set provides different built-in methods to perform mathematical set operations like union, intersection, subtraction, and symmetric difference.      

# We use the | operator or the union() method to perform the set union operation

# first set
A = {1, 3, 5}

# second set
B = {0, 2, 4}

# perform union operation using |
print('Union using |:', A | B)

# perform union operation using union()
print('Union using union():', A.union(B))                   


                        ##################################################################
                            #    Set Intersection
                        ###################################################################

# The intersection of two sets A and B include the common elements between set A and B.

# In Python, we use the & operator or the intersection() method to perform the set intersection operation. 
# first set
A = {1, 3, 5}

# second set
B = {1, 2, 3}

# perform intersection operation using &
print('Intersection using &:', A & B)

# perform intersection operation using intersection()
print('Intersection using intersection():', A.intersection(B)) 




                        ##################################################################
                            #    Difference between Two Sets
                        ###################################################################

# The difference between two sets A and B include elements of set A that are not present on set B.
# We use the - operator or the difference() method to perform the difference between two sets. For example,

# first set
A = {2, 3, 5}

# second set
B = {1, 2, 6}

# perform difference operation using &
print('Difference using &:', A - B)

# perform difference operation using difference()
print('Difference using difference():', A.difference(B)) 


                        ##################################################################
                            #    Set Symmetric Difference
                        ###################################################################

# The symmetric difference between two sets A and B includes all elements of A and B without the common elements.
# In Python, we use the ^ operator or the symmetric_difference() method to perform symmetric differences between two sets. 

# first set
A = {2, 3, 5}

# second set
B = {1, 2, 6}

# perform difference operation using &
print('using ^:', A ^ B)

# using symmetric_difference()
print('using symmetric_difference():', A.symmetric_difference(B))           


# Check if two sets are equal
# We can use the == operator to check whether two sets are equal or not.
# first set
A = {1, 3, 5}

# second set
B = {3, 5, 1}

# perform difference operation using &
if A == B:
    print('Set A and Set B are equal')
else:
    print('Set A and Set B are not equal')