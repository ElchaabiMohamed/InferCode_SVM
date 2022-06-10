def power(base, exp):
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        base *= base
        new_exp = exp - 1
        power(base, new_exp)