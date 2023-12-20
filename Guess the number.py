""" So this is a code that allows you to guess a number while giving 
you clues"""

import random

num_digits = 3
max_guesses = 10

def main():
    print('''Welcome to the 'Guess the number' game
          I will pick a number with 3 digits
          You have 10 guesses
          Here are the clues:
          When I say:        That means:
          Pico               one digit is correct but in a wrong position
          Fermi              one digit is correct and in the right position
          Bagels             no digit is correct''')
    
    while True:
        secretNum = getSecretNum()
        print('I have thought of a number.')
        print('You have 10 guesses to get it.')

        numGuesses = 1
        while numGuesses <= 10:
            guess = ''
            while len(guess) !=  num_digits or not guess.isdecimal():
                print('Guess #{}:'.format(numGuesses))
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > max_guesses:
                print('Sorry, You ran out of guesses')
                print('The secret number was {}'.format(secretNum))
        
        print('Do you want to play again')
        if not input('> ').lower().startswith('y'):
            break

    print('Thanks for playing!!')

def getSecretNum():
    numbers = list('1234567890')
    random.shuffle(numbers)
    SecretNum = ''
    for i in range(num_digits):
        SecretNum += str(numbers[i])
    return SecretNum

def getClues(guess, secretNum):
    if guess == secretNum:
        return 'You got it!!!'
     
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    if len(clues) == '0':
        return 'Bargels'
    else:
        clues.sort()
        return ' '.join(clues)

if __name__ == '__main__':
    main()



