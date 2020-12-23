def swap(number):
    if number == 0:
        return 1
    else:
        return 0


def switchLights(a):
    candles = a
    for i in range(len(candles)):
        if candles[i] == 1:
            for j in range(i+1):
                candles[j] = swap(candles[j])

    return candles
