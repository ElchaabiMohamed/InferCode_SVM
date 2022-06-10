def minimum(ints):
    if len(ints) == 1:
        return ints[0]
    elif ints[0] > ints[1]:
        ints.remove(ints[0])
    else:
        ints.remove(ints[1])
    return minimum(ints)