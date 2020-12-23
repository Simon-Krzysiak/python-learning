def minimalNumberOfCoins(coins, price):
    nr_coins = 0
    rem = price
    i = len(coins)-1

    while rem > 0:
        new_coins, rem = divmod(rem, coins[i])
        nr_coins += new_coins
        i -= 1
    return nr_coins
