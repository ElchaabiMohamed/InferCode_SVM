def minimum(li):
    if len(li) == 1:
        return li[0]

    if li[0] < li[-1]:
        li[-1] = li[0]
    return minimum(li[1:])
