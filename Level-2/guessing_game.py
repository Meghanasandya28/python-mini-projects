import random

def guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    print("Guess the number between 1 and 100")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            else:
                print(f"Correct! You guessed in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")
if __name__ == "__main__":
    guessing_game()