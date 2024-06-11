###############################################################
# Python Dictionary
################################################################


# Create a Dictionary
# We create a dictionary by placing key: value pairs inside curly brackets {}, separated by commas. For example,

country_capitals = {
    "kenya" : "nairobi",
    "tanzania" : "daar",
    "somalia" : "mogadishu",

}
print(country_capitals)


# Dictionary keys must be immutable, such as tuples, strings, integers, etc. We cannot use mutable (changeable) objects such as lists as keys.
# We can also create a dictionary using a Python built-in function dict(). To learn more, visit Python dict().


country_capitals = {
  "Germany": "Berlin", 
  "Canada": "Ottawa", 
  "England": "London"
}

# access the value of keys
print(country_capitals["Germany"])    
print(country_capitals["England"])    



# Add Items to a Dictionary
country_capitals = {
  "Germany": "Berlin", 
  "Canada": "Ottawa", 
}

country_capitals["Italy"] = "Rome"

print(country_capitals)


# Remove Dictionary Items\
country_capitals = {
  "Germany": "Berlin", 
  "Canada": "Ottawa", 
}


del country_capitals["Germany"]

print(country_capitals)


# Change Dictionary Items
country_capitals = {
  "Germany": "Berlin", 
  "Italy": "Naples", 
  "England": "London"
}


country_capitals["Italy"] = "Rome"

print(country_capitals)

# Iterate Through a Dictionary
country_capitals = {
  "United States": "Washington D.C.", 
  "Italy": "Rome" 
}


for country in country_capitals:
    print(country)

print()


for country in country_capitals:
    capital = country_capitals[country]
    print(capital)




# Find Dictionary Length
country_capitals = {"England": "London", "Italy": "Rome"}


print(len(country_capitals))   

numbers = {10: "ten", 20: "twenty", 30: "thirty"}


print(len(numbers))            

countries = {}


print(len(countries))    


# Dictionary Membership Test
file_types = {
    ".txt": "Text File",
    ".pdf": "PDF Document",
    ".jpg": "JPEG Image",
}

# use of in and not in operators
print(".pdf" in file_types)       
print(".mp3" in file_types)       
print(".mp3" not in file_types)   