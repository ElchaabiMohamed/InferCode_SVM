def swap(a,i,j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp
    return a[i], a[j]
    
def reverse(a):
    i = 0
    while i < len(a) / 2:
        swap(a,i,len(a) - i - 1)
        i = i + 1
    return a
        
def main():
    print(swap([1,2,3], 2, 0))
    print(reverse([4,5,6,7,8]))
    
if __name__ == "__main__":
    main()