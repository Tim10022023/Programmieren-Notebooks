import random

def numberguessing():
    true_number = random.randint(1, 100)
    guesses = 0

    print("A number between 1 and 100 is the solution. Guess it!")

    while True:
        user_input = int(input("Your guess: "))
        guesses += 1

        if user_input < true_number:
            print("Try a higher number")
        elif user_input > true_number:
            print("Try a smaller number")
        else:
            print(f"Congrats! You guessed the number {true_number} in {guesses} tries.")
            break

if __name__ == "__main__":
    numberguessing()
