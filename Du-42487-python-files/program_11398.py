def selection_sort(a):
    i = 0
    while i < len(a):
        p = i
        j = i + 1
        while j < len(a):
            if a[j] < a[p]:
                p = j
            j = j + 1

    tmp = a[p]
    a[p] = a[i]
    a[i] = tmp

    i = i + 1
    i = 0
    while i < len(a):
        print(a[i])
        i += 1
    return a

def main():
   print(double(5))
   print(double("Hello"))

if __name__ == "__main__":
   main()