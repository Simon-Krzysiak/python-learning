"""Task:
    Given an array that contains only numbers in the range from 1 to
    array.length, find the first duplicate number for which the second
    occurrence has the minimal index. In other words, if there are more than
    1 duplicated numbers, return the number for which the second occurrence
    has a smaller index than the second occurrence of the other number does.
    If there are no such elements, return -1."""


def firstDuplicate(array):

    for i in range(len(array)):
        if array[abs(array[i]) - 1] < 0:
            return abs(array[i])
        else:
            array[abs(array[i]) - 1] *= -1

    return -1
