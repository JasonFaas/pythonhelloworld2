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


assert 'abcdefghijklmnopqrstuvwxyz' == getAvailableLetters([])
assert 'abcdfghjlmnoqtuvwxyz' == getAvailableLetters(['e', 'i', 'k', 'p', 'r', 's'])

# abcdefghijklmnopqrstuvwxyz
# print(string.ascii_lowercase)
