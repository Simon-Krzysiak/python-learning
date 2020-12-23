def are_friends(nr1, nr2, divisors):
    for divisor in divisors:
        if not ((nr1 % divisor == 0) == (nr2 % divisor == 0)):
            return False
    return True


def numberOfClans(divisors, k):
    clans = dict()
    clan_count = 0

    for new_num in range(1, k+1):
        for num in clans:
            if are_friends(new_num, num, divisors):
                clans[new_num] = clans[num]
                break
        if new_num not in clans:
            clan_count += 1
            clans[new_num] = clan_count

    return clan_count
