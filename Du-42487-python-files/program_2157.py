def bsearch(a, q):

    found = False
    newSet = q

    while found != True or newSet > 0:
        midpoint = int(len(newSet)/2)
        if a < newSet[midpoint]:
            found = False
            newSet = newSet[:midpoint]
        elif a > newSet[midpoint]:
            found = False
            newSet = newSet[midpoint:]
        elif a==newSet[midpoint]:
            found = True
    return found