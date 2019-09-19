"""
Simple function that will test if inputted year is a leap year
William Alber 9/19/2019
"""

def is_hebrew_leap_year(year):
    remain = year % 19
    if remain in {0, 3, 6, 8, 11, 14, 17}: # simple tuple to test all
        print("Leap Year!")
    else: # if remain isn't one of the others
        print("Not a leap year...")

print(is_hebrew_leap_year(5779))
