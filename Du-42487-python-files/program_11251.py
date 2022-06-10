from time import sleep

def power(base, exp, mult = None):
    if mult is None:
        mult = base
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        new_base = base * mult
        new_exp = exp - 1
        return power(new_base, new_exp, mult)


def main():
    print((power(8, 0)))
    print((power(8, 1)))
    print((power(8, 2)))
    print((power(2, 3)))
    print((power(4, 4)))
    print((power(2, 32)))
    print((power(10, 3)))

if __name__ == '__main__':
    main()

