def reverse(l):
    if l == []:
        return []

    temp = reverse(l[1:])
    temp.append(l[0])
    return temp