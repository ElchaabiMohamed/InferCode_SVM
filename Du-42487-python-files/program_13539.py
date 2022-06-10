def power(i, power):
    if i == i**power:
        print(i)
        return i
    power(i * i, power)