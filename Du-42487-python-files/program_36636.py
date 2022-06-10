def swap(a,i,j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp
    
def position_of_smallest(a,i):
    p = i
    j = i + 1
    while j < len(a):
        if j < p:
            p = j
        j = j + 1
    return p
    
def selection_sort(a):
    i = 0
    while i < len(a):
        p = position_of_smallest(a,i)
        swap(a,i,p)
        i = i + 1
        
def main():
    print(swap([1,5,8],2,3))
    print(position_of_smallest([3,4,1],8))
    print(selection_sort([1,2,3]))
    
if __name__ == "__main__":
    main()
    