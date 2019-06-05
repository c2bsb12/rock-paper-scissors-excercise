# game.py

print("Rock, Paper, Scissors, Shoot!") 

#capture input
user_choice = input("Choose your warrior: 'rock', 'paper' or 'scissors' (without the quotes)")

print("__________________________")
print("USER CHOICE:FAILURE", user_choice)


#validate input



if user_choice in ["rock", "paper", "scissors"]:
    print("VALID")
else:
    print("INVALID SELECTION. PLEASE TRY AGAIN")
    exit()

#generate computer selection

print("GENERATING...")

#determine the winner

#display final outputs/outcomes