# lab03.py
import random


def generate_mad_lib(adjective, noun, verb):
    """Return a nonempty story containing all three supplied words."""
    return (
        f"Once upon a time, a {adjective} {noun} decided to {verb} "
        f"across the kingdom. Everyone who saw the {adjective} {noun} "
        f"{verb} agreed it was a sight to remember."
    )


def guessing_game():
    """Run an interactive number-guessing game."""
    secret_number = random.randint(1, 100)
    print("I'm thinking of a number between 1 and 100.")

    while True:
        guess = int(input("Enter your guess: "))

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Correct! Congratulations, you won!")
            break


if __name__ == "__main__":
    guessing_game()
