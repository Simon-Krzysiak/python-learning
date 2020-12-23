import math


def constructSquare(s):
    squares = dict()

    for i in range(1, int(math.sqrt(10**len(s)))+1):
        number = i*i
        dic = dict()
        for digit in str(number):
            dic[digit] = dic.get(digit, 0) + 1
        lis = list()
        for key in dic:
            lis.append(dic[key])
        lis.sort()
        freqs = tuple(lis)
        if freqs in squares:
            squares[freqs].append(number)
        else:
            squares[freqs] = [number]

    s_dic = dict()
    for letter in s:
        s_dic[letter] = s_dic.get(letter, 0)+1

    s_freqs = tuple(sorted([s_dic[key] for key in s_dic]))

    if s_freqs in squares:
        return max(squares[s_freqs])
    else:
        return -1
