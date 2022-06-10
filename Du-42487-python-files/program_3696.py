def selection_sort(a):
    for i in range(0, len(a)):
        p = i
        curr_low = p
        while p < len(a):
            if a[p] < a[curr_low]:
                curr_low = p
            p += 1
        tmp = a[i]
        a[i] = a[curr_low]
        a[curr_low] = tmp