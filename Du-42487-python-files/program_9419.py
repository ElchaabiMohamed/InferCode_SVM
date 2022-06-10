def swap(a,i,j):
    tmp = a[i]
    tmp1 = a[j]
    a[i] = tmp1
    a[j] = tmp
    
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