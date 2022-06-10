# Append l1 to l2. If l2 not supplied default to empty list.
def append2list(l1, l2=None):
    if l2 is None:
        l2 = []
        l2.append(l1)
    return l2



