
def reverse_list(l, new_l=None):
    if new_l == None:
        new_l = []
    if len(l) == 0:
        return new_l
    new_l.append(l.pop())
    return reverse_list(l, new_l)
    