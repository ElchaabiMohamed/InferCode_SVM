def minimum(list):
    if len(list) == 1:
        return list[0]
    else:
        return min(list[0],minimum(list[1:]))