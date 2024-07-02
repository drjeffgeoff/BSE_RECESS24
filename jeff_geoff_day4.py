# Dictionaries
# Creating and using dictionaries
# Dictionary methods and operations
"""_summary_

Dictioneries in python are collections of keys and values.
-Unordered
-mutable and 
-indexed by keys

"""

# Example 1: Create a dictionary
#  Create a dictionary for a student persuing software engineering,
# the key must be your name, age, technology interest, course and year of study. put
# you own details.

student_dict = {
    'name': 'Jeff Geoff',
    'age': '30',
    'technology': 'AI and ML',
    'course': 'BSE',
    'year': 'Year3'
}

# print(student_dict['age'])

# Access values

# Modify Values:
# Execise 1: Modify age and techology

# Example2: adding keys and values
# student_dict['email'] = 'jeff.geoff.cis@gmail.com'

# print(student_dict)

# Excercise 2: Remove a key and value from student_dict

# Common Dictionary methods
"""_summary_
get() // returns the value for the specified key if the key is in the dictionary. 
if not it returns the default value

update() //  Updates the dictionary with the elements from another dictionary

pop() // Removes th specified key and return the corresponding value.


"""
# Example 3: Use the get nethod to get the value

print(student_dict.get('technology'))

# Exercise 3: Use the update nethod to update to change value in age.
# Exercise 4: Use the if to check if the key 'age' is present in the dictionary.

# keys(), values() and the items() methods
print(student_dict.keys())
print(student_dict.values())
print(student_dict.items())

"""_summary_

keys() returns return a view of objects that displays a list of all keys
values() returns a view of objects that displays a list of all values
items() returns a view of objects that displays a list of dictionary keys and 
values tuple pairs


"""

# Exercise5: Use the update method to change course and add a new 
# key "WhatsApp_Number" to the dictionary
