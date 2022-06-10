def maximum(number):
    if len(number) == 1:
        return number[0]

    if number[0] > number[1]:
        number.remove(number[1])
        return maximum(number)

    else:
        number.remove(number[0])
        return maximum(number)