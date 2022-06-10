def power(i, power):
    if i == i**power:
        return i
    power(i * i, power)