def minimum(l):
    mini = 0
    i = 0
    while i < len(l):
        if int(l[i]) <= mini:
            mini = int(l[i])
        i = i + 1
    return mini 