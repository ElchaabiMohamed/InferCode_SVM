def reverse_list(l):
    if len(l) == 0:
        return 0
    else:
        return l[-1] + count_letters(l[:-1])