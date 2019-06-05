# game.py

import random

print("Rock, Paper, Scissors, Shoot!") 

#capture input
user_choice = input("Choose your warrior: 'rock', 'paper' or 'scissors' (without the quotes):")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("USER CHOICE:", user_choice)


#validate input



if user_choice in ["rock", "paper", "scissors"]:
    pass
else:
    print("INVALID SELECTION. PLEASE TRY AGAIN")
    exit()

#generate computer selection

computer_choice = random.choice (["rock", "paper", "scissors"])

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("GENERATING...")
print("COMPUTER CHOICE:", computer_choice)

#determine the winner

#display final outputs/outcomes