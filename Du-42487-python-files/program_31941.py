def swap(a,i,j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp
    return a[i], a[j]
    
def reverse(a):
    i = 0
    j = len(a) - i - 1
    while i < len(a) / 2:
        swap(a,i,j)
        i = i + 1
    return a
    
def main():
    print(swap([3,4,6,7,2], 2,1))
    print(reverse([3,4,6,7,2,1]))
    
if __name__ == "__main__":
    main()