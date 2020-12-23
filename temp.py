def createAnagram(s, t):
    letters_t = dict()
    letters_s = dict()
    
    for char in s:
        letters_s[char] = letters_s.get(char,0) + 1
    
    for char in t:
        letters_t[char] = letters_t.get(char,0) + 1
        
    count = 0
    for char in letters_t:
        count += max(letters_t[char]-letters_s.get(char,0),0)
    return count