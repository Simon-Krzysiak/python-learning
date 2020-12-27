"""Task:
    You have a collection of coins, and you know the values of the coins
    and the quantity of each type of coin in it. You want to know how many
    distinct sums you can make from non-empty groupings of these coins.
"""


def possibleSums(coins, quantity):
    sums = dict()
    sums[0] = None

    for i in range(len(coins)):
        new_sums = dict()
        for val in sums:
            for j in range(quantity[i]+1):
                new_sums.setdefault(val + coins[i]*j, None)
        sums.update(new_sums)

    return len(sums) - 1
