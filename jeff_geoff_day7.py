# Inheritance and Polymorphism
"""_summary_

Inheritance and method overriding
Polymorphism and method resolution
order
Abstract classes and interfaces

"""

# Inheritance and method overriding
"""sumary_line
-- description
Inheritance and method overriding allows a class(child class) to inherit attributes and methods
from another class (parent class).

Key concepts
Base class (parent class): Class whose properties are inherited by another class.
Derived classes (child class): Class that inherits attributes and properties from another base class.

"""

# Example 1: Syntax: Create a class where a dog inherits from animal and overrides with a speak method




import json
import csv
class Animal:
    def speak(self):
        return 'Mwe Mwe Mwe Mwe Mwe Mwe'


class Dog(Animal):
    def speak(self):
        return 'Barks'


# Implementation of inherited classes

# animal = Animal()
# dog = Dog()

# print(animal.speak())
# print(dog.speak())


# Reading and Writing Files


# Polymorphism
# Polymorphism allows objects of different classes to be treated as objects of a common superclass.
# Method Resolution Order (MRO). is order in which python looks for a method in a hierarchy classes.

# Example 2: How polymorphism works in python


class Animal:
    def speak(self):
        return "Croock"


class Dog(Animal):
    def speak(self):
        return "Barks"


class Cat(Animal):
    def speak(self):
        return "Meow"


def make_animal_speak(animal):
    print(animal.speak())


make_animal_speak(Dog())
make_animal_speak(Cat())


# Exercise 1: Create a simple application to manage different types of vehicles. Implement
# derived class to demonstrate inheritance and polymorphism.
"""
Requirements
1. Base class to vehicle
Attributes: make, model and year
Methods: display_info()

2. Derived classes:
Car: inherit from vehicle
attributes: number_of_doors
Overrides: display_info()

Motorcycle: inherit from vehicle
Attributes, type_of_bike (cruiser, sport, touring)
Overrides: display_info()

# Excercise 2: Polymorpism
Create a function that accepts a list of vehicle objects and call their display_info() method
to print details of each vehicle.


"""
# Excercise 2:
# Base Class


class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Vehicle: {self.year} {self.make} {self.model}")

# Derived Class: Car


class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def display_info(self):
        print(f"Car: {self.year} {self.make} {
              self.model}, {self.num_doors} doors")

# Derived Class: Truck


class Truck(Vehicle):
    def __init__(self, make, model, year, payload_capacity):
        super().__init__(make, model, year)
        self.payload_capacity = payload_capacity

    def display_info(self):
        print(f"Truck: {self.year} {self.make} {
              self.model}, Payload Capacity: {self.payload_capacity}kg")

# Derived Class: Motorcycle


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, type_of_bike):
        super().__init__(make, model, year)
        self.type_of_bike = type_of_bike

    def display_info(self):
        print(f"Motorcycle: {self.year} {self.make} {
              self.model}, Type: {self.type_of_bike}")

# Polymorphic Function


def display_vehicle_info(vehicles):
    for vehicle in vehicles:
        vehicle.display_info()


# Test the Implementation
car = Car("Toyota", "Camry", 2022, 4)
truck = Truck("Ford", "F-150", 2021, 1300)
motorcycle = Motorcycle("Harley-Davidson", "Street 750", 2020, "Cruiser")

vehicles = [car, truck, motorcycle]
display_vehicle_info(vehicles)


# Reading and writing  files in Python
"""
1. Working with text files

Handling CSV files
JSON and XML file processing

"""
# 1. Working with text files, open, read, write and close
# Note: Python provides inbuilt functions to handle text files.
# Key cencepts
"""
-- description
Opening File: open() function (r, w, a, r+)
Reading File: read() function
Writing File: write() function
Close File: close() function



"""
# Example 3: Write a file and read a file

# Writing to a text file
with open('jeff.txt', 'w') as file:
    file.write('I am Jeff Geoff and I love Python.\n')
    file.write('I used python for automation')

# Reading from a text file
with open('jeff.txt', 'r') as file:
    content = file.read()
    print(content)


# Handling CSV files
"""
CSV ( Comma Separated Values) file widely for data exchange.

Key Concepts: 
Reading CSV files: Using 'csv.reader()'
Writing CSV files: Using 'csv.writer'
DictReader and DictWriter: The class read and write CSV files as dictionaries


"""
# Example 4: Writing and Reading CSV files


# Writing to a CSV file
with open('jeff.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['name', 'position', 'course'])
    writer.writerow(['Jeff Geoff', 'Lecturer', 'BSE'])
    writer.writerow(['Elsa Nankya', 'Student', 'BSE'])
    writer.writerow(['Hillal Sserunjogi', 'Student', 'BSE'])


# Read from a CSV file
with open('jeff.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)

# JSON and XML file processing
"""sumary_line

JSON ( Javascript Object Notation ) and XML ( eXtensible Markup Language ) are  formats used to  
structure data.

Key Concepts
Loading JSON Data: using json.load() for reading JSON file
Dumping JSON Data: using json.dump() for writing JSON file
Parsing JSON Data: using json.loads() for handling JSON strings

"""

# Example 6: Write and read JSON file

# writing to a JSON file

student_data = {
    'name': 'ahaabwe',
    'course': 'BSE',
    'year': 'Year2'
}

# Open the file
with open('student_data.json', 'w') as json_file:
    json.dump(student_data, json_file)


# Reading the JSON file
with open('student_data.json', 'r') as json_file:
    student_data = json.load(json_file)
    print(student_data)


# Exercise 2: Write and read the xml file.

# Exercise 3: Using abstraction calculate the area and perimeter of a rectangle
