"""
This file contains examples of if-else statements.
"""

# Define a variable with a number
number = 10

# Check if the number is greater than 5
if number > 5: # Here, (number > 5) is a conditional statement
    print("The number is greater than 5.") # This line is executed if the condition is true
else:
    print("The number is not greater than 5.") # This line is executed if the condition is false

# Define a variable with a string
word = "Hello"

# Use an if-else condition to check if the word is "Hello"
if word == "Hello":
    # This block of code will be executed if the condition is true
    print("The word is Hello.")
else:
    # This block of code will be executed if the condition is false
    print("The word is not Hello.")


# Define some variables
a = 10
b = 20
c = 30

# Use the 'and' operator to check if 'a' is less than 'b' AND 'b' is less than 'c'
if (a < b) and (b < c):
    print("Both conditions are true.")

# Use the 'or' operator to check if 'a' is less than 'b' OR 'a' is equal to 'c'
if (a < b) or (a == c):
    print("At least one of the conditions is true.")
