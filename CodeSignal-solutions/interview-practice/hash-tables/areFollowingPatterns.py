"""Task:
    Given an array strings, determine whether it follows the sequence given
    in the patterns array. In other words, there should be no i and j for
    which strings[i] = strings[j] and patterns[i] ≠ patterns[j] or for
    which strings[i] ≠ strings[j] and patterns[i] = patterns[j].
"""


def areFollowingPatterns(strings, patterns):
    str_to_pat = dict()
    pat_to_str = dict()

    for i in range(len(strings)):
        strn = strings[i]
        pat = patterns[i]
        if strn != pat_to_str.setdefault(pat, strn):
            return False
        elif pat != str_to_pat.setdefault(strn, pat):
            return False
    return True
