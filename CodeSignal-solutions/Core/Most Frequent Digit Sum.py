def sum_digits(number):
    return sum([int(d) for d in str(number)])


def step(number):
    return number - sum_digits(number)


def mostFrequentDigitSum(n):
    freqs = dict()
    number = n

    while number > 0:
        freqs[sum_digits(number)] = freqs.get(sum_digits(number), 0) + 1
        number = step(number)

    max_freq = max(freqs.values())
    return max([key for key in freqs if freqs[key] == max_freq])
