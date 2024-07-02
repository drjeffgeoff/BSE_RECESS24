# Defining Functions

# Function syntax and parameters
# Return values
# Lambda functions

# Functions in python are defined using the 'def' keyword, followed by function name
# parentheses (), inside the parentheses you put a parameter name, and the colon.

# Example 1:
def multiply(a, b):
    return a * b


result = multiply(5, 10)
print(result)

# Example 2:  Multiple return values


def get_coordinates():
    return 10, 20


x, y = get_coordinates()
print(x, y)


# Exercise 1: Define a function greet with a parameter name, set to 'Guest', and print a message
# I am a software programmer


def greet(name="Jeff"):
    print(f"I am a software programmer , {name}")


greet()


# Example 3: Return multiple return values
def get_name_and_position():
    name = 'Jeff Geoff,'
    position = 'I am a software programmer'
    return name, position


name, position = get_name_and_position()
print(name, position)

# Exercise 4: Return multiple return values of your name and  age


# Notes
"""_summary_

def: Keyword to define a function
function_name: Name of the function
parameters: Optional, arguments passed to the function
Docstrings: Optional, describes the function purpose
return: optional, renturns a value from the function

 """

# Syntax for defining a function
#  def function_name(parameters):
#      """Docstring Optional"""
#      # Function body
#      return value

# Lambda function
# Lambda function are small anonymous functions defined using the lambda keyword.\
# They are restricted to a single expression

# Syntax for lambda function
# lambda parameter: expression

# Example 5: Create a lambda function to add two numbers


def add(a, b): return a + b


print(add(45, 70))

# Example 6: Use cases of lambda function for sorting

coordinates = [(1, 2), (2, 3), (3, 1), (5, 0)]

coordinates.sort(key=lambda coordinate: coordinate[1])
print(coordinates)


# Map, Filter and Reduce
# Example 6: Get the squares of 1 to 5 using map, filter and reduce

number_squares = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x**2, number_squares))

print(squares)

# Exercise 4: Define a function to get user info that accepts arbitrary keyword arguments and prints
# each key value pair

# **kwargs: Allows passing an arbitrary number of keyword arguments to a function.


# Example 7: How to  handle a **kwargs in Functions

def ahaabwe_function(a, b, **kwargs):
    print(f"a: {a}, b: {b}")

    for key, value in kwargs.items():
        print(f"{key}:{value}")


ahaabwe_function(1, 2, x=100, y=200, z=300)
