def areSimilar(a, b):
    nr_diff = 0
    diffs = list()

    for i in range(len(a)):
        if a[i] != b[i]:
            nr_diff += 1
            if nr_diff > 2:
                return False
            diffs.append((a[i], b[i]))

    if nr_diff == 1:
        return False
    elif nr_diff == 0:
        return True
    else:
        return diffs[0] == diffs[1][::-1]
