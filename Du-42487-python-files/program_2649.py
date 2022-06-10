def power(i, n):
    if i == i**n:
        print(i)
        return i
    i *= i
    power(i, n)
