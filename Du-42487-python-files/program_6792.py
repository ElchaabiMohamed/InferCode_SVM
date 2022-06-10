a = [1, 2, 3, 1, 2, 3]

def selection_sort(a):
    i = 0
    while i < len(a):
        p = i
        j = i + 1
        while j < len(a):
            if a[p] > a[j]:
                p = j
            j += 1

        tmp = a[i]
        a[i] = a[p]
        a[p] = tmp
        i += 1

def main():
    print(a)

if __name__ == "__main__":
    main()



