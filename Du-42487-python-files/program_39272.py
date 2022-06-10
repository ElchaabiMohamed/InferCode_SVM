def swap(a,i,j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = a[i]
    
def reverse(a):
    i = 0
    while i < len(a) / 2:
        swap(a,i,len(a)-1 - i)
        i = i + 1
        
def main():
    print(swap([1,2,3,4,5], 2, 4))
    print(reverse([1,2,3,4,5]))
    
if __name__ == "__main__":
    main() 