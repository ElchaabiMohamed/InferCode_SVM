def reverse_list(l, i = 0):
    if i < len(l) // 2:
        l[i], l[-i - 1] = l[-i - 1], l[i]
        return reverse_list(l, i+1)
    else:
        return l