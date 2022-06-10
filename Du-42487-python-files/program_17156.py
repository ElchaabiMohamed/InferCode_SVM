def swap(a,i,j):
    temp = a[i]
    a[j] = a[i]
    a[i] = temp

a = []
i = 0
while i < len(a):
    p = i
    j = i + 1
    while j < len(a):
        if a[j] < a[p]:
            p = j
        j = j + 1

    swap(a,i,p)
    i = i + 1


def reverse(a):
    while j < len(a):
        if a[j] > a[p]:
            p = j
        j = j + 1

a = []
i = 0
while i < len(a):
    p = i
    j = i + 1
    reverse(a)

    swap(a,i,p)
    i = i + 1


def main():
    print(swap(a,1,2))
    print(reverse(a))

if __name__ == "__main__":
   main()
