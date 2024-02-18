import random

def rock_paper_scissors():
    user_choice = input("Choose rock, paper or scissors: ").lower()

    valid_choices = ['scissors', 'rock', 'paper']

    if user_choice not in valid_choices:
        print("Invalid input. Please choose rock, paper or scissors.")
        return

    computer_choice = random.choice(valid_choices)

    print(f"Computer chose {computer_choice}")

    if user_choice == computer_choice:
        print("Draw!")
    elif (
        (user_choice == 'scissors' and computer_choice == 'paper') or
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock')
    ):
        print("You win!")
    else:
        print("You lost!")

# Spiel starten
rock_paper_scissors()
