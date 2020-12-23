import string


def timedReading(maxLength, text):
    words = text.split()
    words = [word.strip(string.punctuation) for word in words if
             word.strip(string.punctuation) != '']

    count = 0
    for word in words:
        if len(word) <= maxLength:
            count += 1

    return count
