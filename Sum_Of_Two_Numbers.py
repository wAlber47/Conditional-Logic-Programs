"""
Asks for two numbers, if sum is bigger than 100, prints "big number"
if sum is less than 100, prints the sum
William Alber 9/19/2019
"""

# Getting the two numbers
x = int(input("What is your first number: "))
y = int(input("What is your second number: "))

# Getting the sum of the numbers to test
add = x + y

if add > 100:
    print("They add up to a big number.")
else:
    print(add)
