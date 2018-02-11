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

assert '_ _ _ _ _' == getGuessedWord('apple', [])
assert '_ pp_ e' == getGuessedWord('apple', ['e', 'i', 'k', 'p', 'r', 's'])
# print(getGuessedWord(secretWord, lettersGuessed))
