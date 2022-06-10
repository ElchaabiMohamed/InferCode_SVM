def reverse_list(l):
    if reverse_list.count == ((len(l)) // 2):
        return l
    x = l.pop(0)
    l.append(x)
    reverse_list.count += 1
    try:
        print((reverse_list.count))
        return reverse_list(l)
    finally:
        reverse_list.count = 0
reverse_list.count = 0
