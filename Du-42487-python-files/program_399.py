def count_letters(a, count = 0):
    if len(a) == 0:
        return count
    count += 1
    return count_letters(a[:-1], count)