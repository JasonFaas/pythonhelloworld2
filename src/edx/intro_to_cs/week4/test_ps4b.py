from ps4b import *

def test_playGame(wordlist):
    # success = False
    # hand = {'h': 1, 'i': 1, 'm': 1}
    # hand = {'h': 1, 'i': 1, 'c': 1, 'z': 1, 'm': 2, 'a': 1}
    # assert len(hand.keys()) == 3
    playGame(wordList)
    print("SUCCESS: test_getWordScore()")



wordList = loadWords()
print("----------------------------------------------------------------------")
print("Testing playGame(wordList)...")
test_playGame(wordList)
print("----------------------------------------------------------------------")
print("All done!")
