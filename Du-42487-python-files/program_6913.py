def selection_sort(a):
    i = 0
    while i < len(a):
        p = i
        j = i + 1
        while j < len(a):
            if a[j] < a[p]:
                p = j
            j += 1       
        
        temp = a[i]
        a[i] = a[p]
        a[p] = temp
    
        i += 1

def main():
    return 0

if __name__ == "__main__":
    main()

