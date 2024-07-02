"""_summary_
Control Structures

Conditional statements (if, elif, else)
Loops (for, while)
Comprehensions (list, dictionary
comprehensions)
"""
# if, elif, else

# age = 70

# if age < 18:
#     print('You are an adult')

# elif age > 65:
#     print('You are senior citizens')

# else:
#     print('You are a youth')


# 90, above above is Excellent, Ea=ual 80 and above is Very good , if 70 , good
# otherwise , not good.
# Example 2:

# grade = 50

# if grade >= 90:
#     print('Excellent')
# elif grade >= 80:
#     print('Very good')
# elif grade >= 70:
#     print('Good')
# else:
#     print('Not good')

"""sumary_line
Exercise: Scenario: Write a python script to determine the price 
of a movie based on age. Condition children under 13 get discount for price
=shs1000
Teenagers between 13 and 18 get discount for price = shs 500
Adults 18 and above  pay full price = shs 2000
Otherwise, senior citizens pay full price = shs 5000


"""
# age = int(input("Enter your age: "))


# if age < 13:

#     print("Invalid age. Please enter a non-negative value.")

# elif age < 13:

#     price = 1000

#     print(f"Teen ager under 13 years old: shs{price}")

# elif age > 13 and age < 18:  # Include 17 years old in the discount

#     price = 1500

#     print(f"Youth between 13 and 17 years old (inclusive): shs{price}")

# elif age >= 18:  # Include 65 years pay full price

#     price = 2000

#     print(f"Youth between 18 and 64 years old (inclusive): shs{price}")

# else:

#     price = 5000

#     print(f"Senior citizens 65 years old and above: shs{price}")


# Loops (for, while)
"""_summary_
for loop iterates over a sequence (list, tuple, dictionary, set, string)
The while loop repeats as long as a condition is true

"""
# Example 3

cars = ['Tesla', 'Audi', 'BMW', 'Jeep', 'RangeRover']

for car in cars:
    print(car)


# Example 4  count 1 to 10

count = 1
while count <= 5:
    print("Count 1 to 5:", count)
    count += 1

# Exercise 2
"""_summary_
    1. Create your own list of favorite colors using for loop
    2. Create a reverse  of the input 12345 to be 54321 using while loop
"""
# Answer

color_list = ['red', 'green', 'blue', 'yellow', 'purple']

# Reversing the list
reversed_color = color_list[::-1]

for color in reversed_color:
    print(color)


# reversing using the while loop

color_list = ['red', 'green', 'blue', 'yellow', 'purple']

# intialise the index to the last element in the list
index = len(color_list) - 1

# Using while loop
while index >= 0:
    print(color_list[index])
    index -= 1
