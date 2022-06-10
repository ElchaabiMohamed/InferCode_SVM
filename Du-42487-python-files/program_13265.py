def minimum(l):
    mini = 0
    i = 0
    while i < len(l)-1:
        if mini > l[i]:
            mini = int(l[i])
        i = i + 1
    return mini