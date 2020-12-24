"""Task:
    A cryptarithm is a mathematical puzzle for which the goal is to find the
    correspondence between letters and digits, such that the given
    arithmetic equation consisting of letters holds true when the letters
    are converted to digits.

    You have an array of strings crypt, the cryptarithm, and an an array
    containing the mapping of letters and digits, solution. The array crypt
    will contain three non-empty strings that follow the structure:
    [word1, word2, word3], which should be interpreted as the
    word1 + word2 = word3 cryptarithm.

    If crypt, when it is decoded by replacing all of the letters in the
    cryptarithm with digits using the mapping in solution, becomes a valid
    arithmetic equation containing no numbers with leading zeroes, the
    answer is true. If it does not become a valid arithmetic solution, the
    answer is false.
"""


def isCryptSolution(crypt, solution):
    sol = dict()
    for (letter, digit) in solution:
        sol[letter] = digit

    nr1_str = ''.join([sol[letter] for letter in crypt[0]])
    nr2_str = ''.join([sol[letter] for letter in crypt[1]])
    nr3_str = ''.join([sol[letter] for letter in crypt[2]])

    nr1 = int(nr1_str)
    nr2 = int(nr2_str)
    nr3 = int(nr3_str)

    if len(nr1_str) != len(str(nr1)):
        return False
    if len(nr2_str) != len(str(nr2)):
        return False
    if len(nr3_str) != len(str(nr3)):
        return False

    return nr1+nr2 == nr3
