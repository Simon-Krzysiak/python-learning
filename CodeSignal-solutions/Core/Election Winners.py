def electionsWinners(votes, k):
    first = 0
    second = 0

    for candidate in votes:
        if candidate >= first:
            first, second = candidate, first
        else:
            second = max(candidate, second)

    count = 0

    for candidate in votes:
        if candidate + k > first:
            count += 1
        elif candidate > second:
            count += 1

    print(first, second)
    return count
