"""
Basic program that takes input from the user to check if they can vote
William Alber 9/19/2019
"""

# Getting input from the user
age = int(input("How old are you: "))

# Testing input from the user
if age < 18:
    print("You must be 18 to vote.")
else:
    print("You are of voting age.")
