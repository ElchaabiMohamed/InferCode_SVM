def power(base, exp):
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        new_base = base * base
        new_exp = exp - 1
        return power(new_base, new_exp)