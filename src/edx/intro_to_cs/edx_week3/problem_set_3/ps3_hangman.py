# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for swChar in secretWord:
        if swChar not in lettersGuessed:
            return False
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    return_string = ''
    for swChar in secretWord:
        if swChar not in lettersGuessed:
           return_string = return_string + '_ '
        else:
            return_string += swChar
    return return_string.strip()



import string


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    lowercase = string.ascii_lowercase
    for charGuessed in lettersGuessed:
        lowercase = lowercase.replace(charGuessed, '')
    return lowercase
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is %s letters long." % len(secretWord))
    guess_count = 8
    guessed_letters = []
    while guess_count > 0 and not isWordGuessed(secretWord, guessed_letters):
        print("-------------")
        print("You have %s guesses left." % guess_count)
        values = getAvailableLetters(guessed_letters)
        print("Available letters: %s" % values)
        current_guess_letter = input("Please guess a letter: ").lower()[0:1]
        instant_reply = ""
        if current_guess_letter in guessed_letters:
            instant_reply = "Oops! You've already guessed that letter: "
        elif current_guess_letter in secretWord:
            instant_reply = "Good guess: "
        else:
            instant_reply = "Oops! That letter is not in my word: "
            guess_count -= 1
        guessed_letters.append(current_guess_letter)
        print(instant_reply + getGuessedWord(secretWord, guessed_letters))
    print("-------------")
    if isWordGuessed(secretWord, guessed_letters):
        print("Congratulations, you won!")
    else:
        print("Sorry, you ran out of guesses. The word was %s." % secretWord)



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
