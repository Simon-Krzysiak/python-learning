"""Task:
    Given a string and array of pairs that indicates which indices (1-based)
    in the string can be swapped, return the lexicographically largest
    string that results from doing the allowed swaps. You can swap indices
    any number of times.
"""

from copy import deepcopy as deepcopy


def swapLexOrder(string, pairs):
    groups = sorted([set(pair) for pair in pairs])
    used = dict()
    prev_groups = []

    while prev_groups != groups:
        for group in groups:
            for nr in group:
                if nr not in used:
                    used[nr] = deepcopy(group)
                else:
                    for nr2 in used:
                        if nr in used[nr2] and nr != nr2:
                            used[nr].update(used[nr2])
                            used[nr2].update(group)

        prev_groups = deepcopy(groups)
        groups = list()
        for val in used.values():
            if val not in groups:
                groups.append(deepcopy(val))

    letters = list(string)
    for group in groups:
        let = list()
        indices = list()
        for index in group:
            let.append(letters[index-1])
            indices.append(index-1)
        let.sort(reverse=True)
        indices.sort()
        for i in range(len(indices)):
            letters[indices[i]] = let[i]
    return ''.join(letters)
