

###################################################################################################
                            # Python Directory and Files Management
###################################################################################################



# A directory is a collection of files and subdirectories. A directory inside a directory is known as a subdirectory.
# Python has the os module that provides us with many useful methods to work with directories (and files as well).


######## Get Current Directory in Python
# We can get the present working directory using the getcwd() method of the os module.
# This method returns the current working directory in the form of a string. For example,

import os
print(os.getcwd())
# Here, getcwd() returns the current directory in the form of a string.

#####################3 Changing Directory in Python
# In Python, we can change the current working directory by using the chdir() method.

# The new path that we want to change into must be supplied as a string to this method. And we can use both the forward-slash / or the backward-slash \ to separate the path elements.

# Let's see an example,
import os

# change directory
# os.chdir('C:\\Python33')

print(os.getcwd())



# All files and sub-directories inside a directory can be retrieved using the listdir() method.

################### Making a New Directory in Python

# In Python, we can make a new directory using the mkdir() method.
# This method takes in the path of the new directory. If the full path is not specified, the new directory is created in the current working directory.
# os.mkdir('test')

# os.listdir()
# ['test']

#################### Renaming a Directory or a File

# The rename() method can rename a directory or a file.
# For renaming any directory or file, rename() takes in two basic arguments:
# the old name as the first argument
# the new name as the second argument.
# import os

# os.listdir()
# ['test']

# # rename a directory
# os.rename('test','new_one')

# os.listdir()
# ['new_one']


######################## Removing Directory or File in Python

# n Python, we can use the remove() method or the rmdir() method to remove a file or directory.
# First let's use remove() to delete a file,
# import os

# # delete "myfile.txt" file
# os.remove("myfile.txt")

# # Here, we have used the remove() method to remove the "myfile.txt" file.
# # Now let's use rmdir() to delete an empty directory,
# import os

# # delete the empty directory "mydir"
# os.rmdir("mydir") 

# # In order to remove a non-empty directory, we can use the rmtree() method inside the shutil module. For example,
# import shutil

# # delete "mydir" directory and all of its contents
# shutil.rmtree("mydir")


# It's important to note that these functions permanently delete the files or directories, so we need to careful when using them.







####################################################################################################################################
                                            # Python CSV: Read and Write CSV Files
####################################################################################################################################

# The CSV (Comma Separated Values) format is a common and straightforward way to store tabular data. To represent a CSV file, it should have the .csv file extension.

# Now, let's proceed with an example of the info .csv file and its data.

# SN, Name,    City
# 1,  Michael, New Jersey
# 2,  Jack,    California



#################  Working With CSV Files in Python

# Python provides a dedicated csv module to work with csv files. The module includes various methods to perform different operations.
# However, we first need to import the module using:
import csv


############################ Read CSV Files with Python
# The csv module provides the csv.reader() function to read a CSV file.

# Name,   Age, Profession
# Jack,   23,  Doctor
# Miller, 22,  Engineer

# Now, let's read this csv file.
import csv

with open('people.csv', 'r') as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

# Output

['Name', 'Age', 'Profession']
['Jack', '23', 'Doctor']
['Miller', '22', 'Engineer']  

# Here, we have opened the people.csv file in reading mode using:

# with open(airtravel.csv', 'r') as file:
          
# We then used the  csv.reader() function to read the file. To learn more about reading csv files, Python Reading CSV Files.

############################# Write to CSV Files with Python

# The csv module provides the csv.writer() function to write to a CSV file.
# Let's look at an example.

import csv
with open('protagonist.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SN", "Movie", "Protagonist"])
    writer.writerow([1, "Lord of the Rings", "Frodo Baggins"])
    writer.writerow([2, "Harry Potter", "Harry Potter"])          


# When we run the above program, a protagonist.csv file is created with the following content:



# In this example, we have created the CSV file named protagonist.csv in the writing mode.

# We then used the csv.writer() function to write to the file. To learn more about writing to a csv file, Python Writing CSV Files.

# Here,

# writer.writerow(["SN", "Movie", "Protagonist"]) writes the header row with column names to the CSV file.
# writer.writerow([1, "Lord of the Rings", "Frodo Baggins"]) writes the first data row to the CSV file.
# writer.writerow([2, "Harry Potter", "Harry Potter"]) writes the second data row to the CSV file.

##########################################################################################################################
                                # Using Python Pandas to Handle CSV Files
##########################################################################################################################

# Pandas is a popular data science library in Python for data manipulation and analysis.

# If we are working with huge chunks of data, it's better to use pandas to handle CSV files for ease and efficiency.           
# 

# Note: Before we can use pandas, we need to install and import it. To learn more, visit Install and Import Pandas.


######################### Read CSV Files
# To read the CSV file using pandas, we can use the read_csv() function.

# import pandas as pd
# pd.read_csv("people.csv")

# Here, the program reads people.csv from the current directory.

############### Write to a CSV Files
# to write to a CSV file, we need to use the to_csv() function of a DataFrame.

# import pandas as pd
# # creating a data frame
# df = pd.DataFrame([['Jack', 24], ['Rose', 22]], columns = ['Name', 'Age'])
# # writing data frame to a CSV file
# df.to_csv('person.csv')

# Here, we have created a DataFrame using the pd.DataFrame() method. Then, the to_csv() function for this object is called, to write into person.csv.



#########################################################################################################################
                                        # Reading CSV files in Python
#########################################################################################################################

# We are going to exclusively use the csv module built into Python for this task. But first, we will have to import the module as :

# Example 1: Read CSV files with csv.reader()
import csv
with open('innovators.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


# output
['SN', 'Name', 'Contribution']
['1', 'Linus Torvalds', 'Linux Kernel']
['2', 'Tim Berners-Lee', 'World Wide Web']
['3', 'Guido van Rossum', 'Python Programming']        
# Here, we have opened the innovators.csv file in reading mode using open() function.


################### CSV files with Custom Delimiters
# By default, a comma is used as a delimiter in a CSV file. However, some CSV files can use delimiters other than a comma. Few popular ones are | and \t.

# Suppose the innovators.csv file in Example 1 was using tab as a delimiter. To read the file, we can pass an additional delimiter parameter to the csv.reader() function.

########################### Example 2: Read CSV file Having Tab Delimiter
import csv
with open('innovators.csv', 'r') as file:
    reader = csv.reader(file, delimiter = '\t')
    for row in reader:
        print(row)
# Output

['SN', 'Name', 'Contribution']
['1', 'Linus Torvalds', 'Linux Kernel']
['2', 'Tim Berners-Lee', 'World Wide Web']
['3', 'Guido van Rossum', 'Python Programming']

# As we can see, the optional parameter delimiter = '\t' helps specify the reader object that the CSV file we are reading from, has tabs as a delimiter.

#########################  CSV files with initial spaces
# ome CSV files can have a space character after a delimiter. When we use the default csv.reader() function to read these CSV files, we will get spaces in the output as well.

# To remove these initial spaces, we need to pass an additional parameter called skipinitialspace. Let us look at an example:

####################### Example 3: Read CSV files with initial spaces
# Suppose we have a CSV file called people.csv with the following content:

# SN, Name, City
# 1, John, Washington
# 2, Eric, Los Angeles
# 3, Brad, Texas
# We can read the CSV file as follows:

import csv
with open('people.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, skipinitialspace=True)
    for row in reader:
        print(row)

# Output

['SN', 'Name', 'City']
['1', 'John', 'Washington']
['2', 'Eric', 'Los Angeles']
['3', 'Brad', 'Texas']        


# The program is similar to other examples but has an additional skipinitialspace parameter which is set to True.

# This allows the reader object to know that the entries have initial whitespace. As a result, the initial spaces that were present after a delimiter is removed.







#####################################################################################################################################
##########################  READ ON CSV ON READING AND WRITTING #####################################################################
#####################################################################################################################################