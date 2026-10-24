import random

print("================================")
print("     NUMBER GUESSING GAME")
print("================================")

while True:
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    print("\nI have selected a number between 1 and 100.")
    print("Try to guess the number!")

    # Continue until the user guesses correctly
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                attempts -= 1
                continue

            if guess < secret_number:
                print("Too low! Try a higher number.")

            elif guess > secret_number:
                print("Too high! Try a lower number.")

            else:
                print("\nCongratulations! You guessed the number!")
                print("The correct number was:", secret_number)
                print("Total attempts:", attempts)
                break

        except ValueError:
            print("Invalid input! Please enter a whole number.")

    # Ask whether the user wants another round
    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("\nThank you for playing!")
        print("Game Over!")
        break