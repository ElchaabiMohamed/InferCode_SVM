def swap(a, i, p):
    tmp = a[i]
    a[i] = a[p]
    a[p] = tmp


def selection_sort(a):
    i = 0
    while i < len(a):
        p = i
        j = i + 1
        while j < len(a):
            if a[j] < a[p]:
                p = j
            j = j + 1

        swap(a, i, p)

        i = i + 1

    return a

def main():
    a = [6, 1, 4, 5, 3, 7]
    print(selection_sort)

if __name__ == "__main__":
   main()
