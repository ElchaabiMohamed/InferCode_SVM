def reverse_list(a, b = ''):
    if a == []:
        return b.strip.split(' ')
    b += ' ' + str(a[-1])
    return reverse_list(a[:-1], b)