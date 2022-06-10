def reverse_list(l):
    if len(l) == 0:
        return reverse_list.m
    reverse_list.m.append(l.pop())
    try:
        return reverse_list(l)
    finally:
        reverse_list.m = []
reverse_list.m = []


