def append2list(l1, l2=None):
    if l2 is None:
        l2 = []
        for i in l1:
            l2.append(l1)
        return l2
    else:
        return [l1 , l2]




