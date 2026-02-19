import random

def show_rules():
    print("\n===== ROCK PAPER SCISSORS GAME =====")
    print("Rules:")
    print("Rock beats Scissors")
    print("Scissors beats Paper")
    print("Paper beats Rock")
    print("-----------------------------------")

choices = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0

show_rules()

while True:
    user_choice = input("\nEnter rock, paper, or scissors: ").lower()

    if user_choice not in choices:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        continue

    computer_choice = random.choice(choices)

    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("Result: It's a tie!")

    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("Result: You Win!")
        user_score += 1

    else:
        print("Result: You Lose!")
        computer_score += 1

    print("\nScoreboard:")
    print("You:", user_score)
    print("Computer:", computer_score)

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("\nFinal Score:")
        print("You:", user_score)
        print("Computer:", computer_score)
        print("Thank you for playing!")
        break
