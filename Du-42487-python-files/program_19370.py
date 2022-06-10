def reverse_list(n):
    if len(n) == 1:       
        return n
    else:
        return [n[-1]] + reverse_list(n[:-1])
