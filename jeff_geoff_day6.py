# Error Handling in Python
# Exception Handling with try, except, else, and finally
# Custom exceptions

"""_summary_

Notes:
Error handling in Python it helps to handle unexpected situations and errors.

1. Try: contains code that might throw an exception
NB: If an exception is occurs the rest of the code in the try block is skipped or ignored

2. Except: catches and handles exceptions
NB: You can specify different handlers fo different exceptions types

3. Else: the code runs if no exception occurs 
If no exception are raised in the try block it runs.

4. Finally: It runs whether an exception is raised/occurred or not
NB: Used for cleaning up actions

"""
# Example 1: Handle exceptions with division by zero.

try:
    number = int(input('Enter a number: '))
    result = 20 / number

except ValueError:
    print("Invalid number! Please enter a valid number")

except ZeroDivisionError:
    print("Error! Division by zero is not allowed")

else:
    print(f"Result is {result}")

finally:
    print("Execution completed successfully")


# Exercise 1: Write a function that converts a string to an integer and handle both valueError
# if a the string cannot be converted to an integer and the TypeError if the input is not a string.
# Use multiple except block to handle these execeptions.

# Custom exception handling
# Example 2: Exeception raised for error in the input, if funds are insufficient.

class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.message = f"Attempt to withdraw {
            self.amount} with only {self.balance} in account"
        super().__init__(self.message)


def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount


# Custom exceptions handling
try:
    balance = 20000
    amount_to_withdraw = 12000
    new_balance = withdraw(balance, amount_to_withdraw)

except InsufficientFundsError as e:
    print('Error: {e.message}')


else:
    print(f"Widthdrawal Successfully! New Balance is {new_balance} ")


finally:
    print("Transaction completed")


# Note:
""""sumary_line

### Defining a Custom Exception

Class CustomError(Exception):
 #Custom Exception for specific error cases
 
 def __init__(self,message):
    super().__init__(message)
    self.message = message

### Raising a Custom Exception
def check_value(value):
    if value is < 0 or value:
        raise CustomError("Value cannot be negative")
    return value
    
# Handle exceptions with try, except, else, and finally   
try:
result = check_value(-10)

except CustomError as e:
    print(f"Custom error caught: {e.message}")

"""

# Excercise 2: Create a custom exception InvalidAgeError  and write a  function that raises
# this exception if the given age is negative. Handle this custom exception when calling the function.
