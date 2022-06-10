def reverse_list(li, n=0):
    if n == int(len(li) / 2):
        return li
    else:
        li[n], li[-n-1] = li[-n-1], li[n]
        return reverse_list(li, n+1)