def swap(a,i,j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp

def reverse(a):
    i = 0
    while i < len(a) / 2:
        j = len(a) - 1 - i
        swap(a, i, j)
        i += 1
    return a

def main():
    a = [9, 8, 7, 1, 2, 3]
    print(reverse(a))

if __name__ == "__main__":
    main()