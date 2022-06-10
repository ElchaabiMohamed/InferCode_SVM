def count_letters(s, n=0):
    if len(s) == 0:
        return n
    return count_letters(s[1:], n+1)