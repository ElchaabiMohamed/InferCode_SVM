def power(base, ind):

    if ind == 0:
        return 1

    return base * power(base, (ind - 1))
