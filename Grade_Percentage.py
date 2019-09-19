"""
Takes input from the user and prints out the associated letter grade
William Alber 9/19/2019
"""

# Getting number grade from the user
grade = int(input("Please enter your grade percentage: "))

# Converting number grade to letter grade and printing
if grade >= 93:
    print("A")
elif grade >= 90:
    print("A-")
elif grade >= 87:
    print("B+")
elif grade >= 83:
    print("B")
elif grade >= 80:
    print("B-")
elif grade >= 77:
    print("C+")
elif grade >= 73:
    print("C")
elif grade >= 70:
    print("C-")
elif grade >= 67:
    print("D+")
elif grade >= 63:
    print("D")
elif grade >= 60:
    print("D-")
else:
    print("F")
