def minimum(value):
    if len(value) == 1:
        return value[0]

    if value[0] < value[1]:
        value.remove(value[1])
        return minimum(value)

    else:
        value.remove(value[0])
        return minimum(value)