def houseNumbersSum(inputArray):
    total = 0
    i = 0
    while inputArray[i] > 0:
        total += inputArray[i]
        i += 1
    return total
