def count_letters(s, count=0):
    if not s:
        return count
    return count_letters(s[:-1], count + 1)
