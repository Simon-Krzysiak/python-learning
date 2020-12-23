def allLongestStrings(inputArray):
    longest_strings = list()
    max_len = max([len(s) for s in inputArray])

    for string in inputArray:
        if len(string) == max_len:
            longest_strings.append(string)
       
    return longest_strings
