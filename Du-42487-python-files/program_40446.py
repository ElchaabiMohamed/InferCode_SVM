def swap(a,i,j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

def reverse(a):
    i = 0
    j = len(a) - 1
    while i < len(a) / 2:
        swap(a,i,j)
        i += 1
        j -= 1 

def main():
    return 0

if __name__ == "__main__":
    main()

