def count_letters(l):
    if len(l) == 0:
        return 0
    else:
        return 1 + count_letters(l[1:])