def count_letters(s, c=0):
    if not s:
        return c
    return count_letters(s[:-1], c + 1)
