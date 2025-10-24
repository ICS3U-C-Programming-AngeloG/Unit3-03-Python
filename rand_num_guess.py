#!/usr/bin/env python3

# Created by: Angelo Garcia
# Created on: October 23rd, 2025
# This program asks the user to guess a number between 0 and 9

import random  # Import the random module to generate a random number


def main():
    # Generate a random number between 0 and 9
    correct_number = random.randint(0, 9)

    # Ask the user to guess a number
    user_guess = int(input("Guess a number between 0 and 9: "))
    print("")

    # Check if the user's guess is correct
    if user_guess == correct_number:
        print("You guessed correctly!")
    else:
        print("You guessed wrong. The correct answer was:", correct_number)


if __name__ == "__main__":
    main()
