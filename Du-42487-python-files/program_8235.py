def selection_sort(a):
    i = 0
    while i < len(a):
        smallest = i
        j = i
        while j < len(a):
            if a[smallest] > a[j]:
                smallest = j
            j = j + 1 
        tmp = a[i]
        a[i] = a[smallest]
        a[smallest] = tmp
        i = i + 1

def main():
    a = [1, 2, 3, 1, 2, 3]
    selection_sort(a)
    print(a)
    
if __name__ == "__main__":
    main()
    


