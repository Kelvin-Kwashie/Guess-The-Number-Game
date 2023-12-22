__author__ = "Kelvin Kwashie"
__credits__ = ["Kelvin Kwashie", "Chris Karvouniaris"]
__version__ = "0.0.1"
__maintainer__ = "Chris Karvouniaris"


""" 
    This is a Guess-the-number game in Python.
    The game is played by only one player at a time.
    The system picks a random 3-digit number.
    The user has 10 tries to guess the selected number.
"""

import random
from collections import Counter


DIGITS_NUM = 3
MAX_GUESSES = 10
FERMI = "Fermi"
PICO = "Pico"
BAGELS = "Bagels"


def welcome_player():
    print(
        f"""
        Welcome to the 'Guess the number' game by {__author__}!
        
        A number with {DIGITS_NUM} digits will be selected
        and you will have {MAX_GUESSES} guesses to find it!

        After each one of your guess, you get some help
        by the available clues.

        Clues meanings:

        Pico               One digit is correct but in a wrong position.
        Fermi              One digit is correct and in the right position.
        Bagels             No digit is correct
        """
    )


def get_secret_number():
    """
    Returns a string made up of 3 unique digits
    """
    digits = [str(number) for number in range(10)]
    random.shuffle(digits)
    return "".join(digits[0:DIGITS_NUM])


def get_guess_input():
    """
    Keeps getting the user input until it is a valid guess
    Returns a string made up of 3 digis
    """

    while True:
        guess = input('> ')
        if not guess.isdecimal():
            print(f"Input was not a number. A {DIGITS_NUM} digit number input is required.")
        elif len(guess) != DIGITS_NUM:
            print(f"A {DIGITS_NUM} digit number input is required. {len(guess)} were given.")
        else:
            return guess


def show_clues(guess_number, secret_number):
    """
    Finds similarities of a guess number and a reference number of same digits
    and gives out clues towards the reference number based on the clues description
    """
     
    clues = []

    for index, digit in enumerate(guess_number):
        if guess_number[index] == secret_number[index]:
            #A correct digit is in the correct place
            clues.append(FERMI)
        elif digit in secret_number:
            #A digit is in the incorrect place
            clues.append(PICO)
    
    print("\nYour clues:")
    if not clues:
        #There are no correct digits at all
        print(f"{BAGELS}")
    else:
        # use build in counter to count instances of each value in list
        # then use the dictionary of counters to present them
        clues = Counter(clues)
        for value, counter in clues.items():
            print(f"{value}: {counter}")


def main():
    """
    Main function of the game.
    """

    welcome_player()

    # The main game loop
    while True: 
        # This creats and holds the secret number the player needs to guess
        secret_number = get_secret_number()
        print("A number has been selected!")
        print(f"You have {MAX_GUESSES} guesses to find it, let's go!")

        player_guesses_counter = 0
        while True:
            print(f"\nGuess #{player_guesses_counter + 1}")
            guess = get_guess_input()

            if guess == secret_number:
                # Number of input was correct finish the round
                print("You got it!!!")
                break

            # Number of input was incorrect
            # Increase guesses counter and give clues
            player_guesses_counter += 1
            if player_guesses_counter < MAX_GUESSES:
                show_clues(guess, secret_number)
            else:
                print("\nSorry, you ran out of guesses :(")
                print(f"The secret number was {secret_number}\n")
                break

        
        #Ask the player if they want to play again
        print("Would you like to play again? (y/n)")
        if not input('> ').lower().startswith('y'):
            break

    print('Thanks for playing!!')


if __name__ == '__main__':
    main()
