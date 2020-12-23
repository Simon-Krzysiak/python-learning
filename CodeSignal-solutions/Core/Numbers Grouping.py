def numbersGrouping(a):
    groups = dict()
    
    for number in a:
        group, rem = divmod(number, 10**4)
        if rem == 0:
            group -= 1
        groups[group] = None

    return len(groups) + len(a)