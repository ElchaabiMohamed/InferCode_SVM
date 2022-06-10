def minimum(l):
    if l == []:
        return []

    temp = minimum(l[1:])
    print(temp)
    if len(temp) == 0 or l[0] > temp[0]:
        temp = [l[0]]

    return temp[0]