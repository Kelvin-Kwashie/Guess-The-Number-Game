""" So this is a code that allows you to guess a number while giving 
you clues"""

import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print('''Welcome to the 'Guess the number' game
          I will pick a number with 3 digits
          You have 10 guesses
          Here are the clues:
          When I say:        That means:
          Pico               one digit is correct but in a wrong position
          Fermi              one digit is correct and in the right position
          Bagels             no digit is correct''')
    
    while True: #The main game loop
        #This stores the secret number the player needs to guess
        Secret_num = getSecretNum()
        print('I have thought of a number.')
        print('You have 10 guesses to get it.')

        Num_guesses = 1
        while Num_guesses <= 10:
            guess = ''
            #keep looping until they enter a valid guess
            while len(guess) !=  NUM_DIGITS or not guess.isdecimal():
                print(f'Guess #{Num_guesses}:')
                guess = input('> ')

            clues = getClues(guess, Secret_num)
            print(clues)
            Num_guesses += 1

            if guess == Secret_num:
                break #They're correct so break out of the loop
            if Num_guesses > MAX_GUESSES:
                print('Sorry, You ran out of guesses')
                print('The secret number was {}'.format(Secret_num))
        #Ask the player if they want to play again
        print('Do you want to play again')
        if not input('> ').lower().startswith('y'):
            break

    print('Thanks for playing!!')

def getSecretNum():
    """Returns a string made up of num_digits unique digits"""
    numbers = list('1234567890')
    random.shuffle(numbers)
    """Get the first num_digits digits in the list for the secret number"""
    SecretNum = ''
    for i in range(NUM_DIGITS):
        SecretNum += str(numbers[i])
    return SecretNum

def getClues(guess, Secret_num):
    """Returns a string with the pico, fermi, bagels, clues for a game and secret number pair"""
    if guess == Secret_num:
        return 'You got it!!!'
     
    clues = []

    for i in range(len(guess)):
        if guess[i] == Secret_num[i]:
            #A correct digit is in the correct place
            clues.append('Fermi')
        elif guess[i] in Secret_num:
            #A digit is in the incorrect place
            clues.append('Pico')
    if len(clues) == '0':
        #There are no correct digits at all
        return 'Bargels'
    else:
        #Sort the clues into alphabetical order so their original order dosen't give information away
        clues.sort()
        #Make a single string from the list of string clues
        return ' '.join(clues)

if __name__ == '__main__':
    main()

"""
 Credits:
Dveloper : Kelvin Kwashie
Refrence : Big Book Small Projects
Under the guidance of Chris Karvouniaris
"""


