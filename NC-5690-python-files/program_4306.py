def quatrePlus100(liste):
    Plus100 = []
    n = 0
    i = 0
    while n < len(liste):
        if liste[n] > 100 and i < 4:
            Plus100 += [liste[n]]
            i += 1
        n += 1
    return Plus100