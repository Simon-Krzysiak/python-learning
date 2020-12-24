"""Task:
    Given a string s consisting of small English letters, find and return the
    first instance of a non-repeating character in it. If there is no such
    character, return '_'.
"""


def firstNotRepeatingCharacter(s):
    hist = dict()
    for letter in s:
        hist[letter] = hist.get(letter, 0) + 1
    for letter in s:
        if hist[letter] == 1:
            return letter
    return '_'
