# -*- coding: utf-8 -*-
"""
Had to revise the whole program since I couldn't get the pygame to actually work \
"""
import random
from generatedWords import words
from HangmanPics import hangmanLives
import string

def randomWord(words):
    word=random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hang(guess):
    global randomWord
    if guess.lower() not in randomWord.lower():
        return True
    else:
        return False

def play():
    word = randomWord(words)
    wordLetters=set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    guessedLetters = set()  # what the user has guessed
    tries=6

    # getting user input
    while len(wordLetters) > 0 and tries > 0:
        # the letters used
        print('You have', tries, 'lives left and you have used these letters: ', ' '.join(guessedLetters))

        # what the word is
        wordList = [letter if letter in guessedLetters else '-' for letter in word]
        print(hangmanLives[tries])
        print('Word so far: ', ' '.join(wordList))

        inputLetter = input('Guess a letter or word: ').upper()
        if inputLetter in alphabet - guessedLetters:
            guessedLetters.add(inputLetter)
            if inputLetter in wordLetters:
                wordLetters.remove(inputLetter)
                print('')

            else:
                tries -=1
                print('\nYour letter,', inputLetter, 'is not in the word.')

        elif inputLetter in guessedLetters:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nThat is not a valid letter.')
        
    # if you fail or guess right
    if tries == 0:
        print(hangmanLives[tries])
        print('You died, sorry. The word was', word)
    else:
        print('YAY! You guessed the word', word, '!!')


if __name__ == '__main__':
    play()