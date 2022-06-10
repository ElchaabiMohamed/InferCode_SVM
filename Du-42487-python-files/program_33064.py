def power(i, power):
    if i == i**power:
        return i
    i *= i
    power(i, power)
