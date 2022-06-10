def reverse_list(l):
    if l == []:
        return []
    return reverse_list(l[1:]) + [l[0]]
    # temp = reverse(l[1:])
    # temp.append(l[0])
    # return temp
    # note we cannot use return reverse(l[1:]).append(l[0]) because append()
    # does not return anything
