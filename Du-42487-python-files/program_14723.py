def count_letters(s):
    if not s:
        return 0
    if len(s) == 1:
        return 1
    return count_letters(s[1:])