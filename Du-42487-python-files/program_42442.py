def selection_sort(a):

    n = input()
    a = []
 
    while n != "end":
        a.append(int(n))
        n =input()
 
    i = 0
    while i < len(a):
        small = i
        j = small + 1
        while j < len(a):
            if a[j] < a[small]:
                small = j
            j += 1
        tmp = a[small]
        a[small] = a[i]
        a[i] = tmp
 
        i += 1
 
    i = 0
    while i < len(a):
        print(a[i])
        i += 1