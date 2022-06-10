def count_letters(s):
    total = 0
    if len(s) == 0:
        return 0

    return 1 + count_letters(s[1:])
