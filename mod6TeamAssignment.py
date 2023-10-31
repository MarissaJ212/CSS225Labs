#Marissa Jones
#10-31-2023

#Mod 6 Team Assignment (Importing and while loop- functions in Pythons)

import random

rand_num = random.randint(1,10)
userGuess = int(input("Guess a number between 1 and 10:"))

if rand_num <=5:
    print("Please guess lower")

else:
    print("Please guess higher")
guess_num = int(input())

if guess_num == rand_num:
    print("Well done, you guessed the correct number!")

else:
    print("You did not guess the correct number, Try again.")
