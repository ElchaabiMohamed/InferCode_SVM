def maximum(list):
    if len(list) == 1:
        return list[0]
    else:
        m = maximum(list[1:])
        return m if m > list[0] else list[0]