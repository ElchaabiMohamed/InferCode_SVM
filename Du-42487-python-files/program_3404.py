def count_letters(string):
    if not string: return 0
    return count_letters(string[1:] + 1)
