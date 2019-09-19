"""
Plays a simple guessing game with the user, with numbers 0-9
William Alber 9/19/2019
"""
from random import randint
random_num = randint(0,9)

# Starts a loop to test guesses efficiently
print("Guess my number between 0-9!")
test = False
while not test:
    # Loop will run until number is guessed
    guess = int(input("What is your guess: "))
    if guess == random_num:
        print("You guessed my number! Nice job!")
        test = True # breaks us out of loop
    else:
        print("Try again!")

