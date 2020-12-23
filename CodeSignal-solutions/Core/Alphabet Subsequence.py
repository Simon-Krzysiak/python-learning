def alphabetSubsequence(s):
    for i in range(len(s)-1):
        if s[i] >= s[i+1]:
            return False
    return True