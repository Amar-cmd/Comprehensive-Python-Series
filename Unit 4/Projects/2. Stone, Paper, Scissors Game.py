# ----------------------------
# ? Stone Paper Scissors Game
# ----------------------------
import random

def get_computer_choice():
    return random.choice(["stone", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"

    elif (user_choice == 'stone' and computer_choice == 'scissors') or (user_choice == "paper" and computer_choice == "stone") or (user_choice == "scissors" and computer_choice == "paper"):
        return "You WIN!"

    else:
        return "Computer Wins"






print("Welcome to Stone, Paper, Scissors Game!")

"""
3. Based on the rule of the game, determine winner
"""

while True:
    user_choice = input("Enter your choice (stone, paper, scissors) or 'quit' to exit: ").lower()

    computer_choice = get_computer_choice()

    if user_choice == 'quit':
        print("Thanks for playing!")
        break

    if user_choice not in ['stone', 'paper', 'scissors']:
        print("Invalid choice. Please Try Again")
        continue

    print(f"Computer Chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)

    print(result)







