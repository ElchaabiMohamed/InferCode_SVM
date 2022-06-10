def swap(a, i, j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp
    return a

def reverse(a):
    i = 0
    while i < len(a) / 2:
        j = len(a) - 1 - i
        swap(a, i, j)
        i = i + 1
    return a

def main():
    a = [2, 3, 1, 4]
    print(reverse(a))

if __name__ == "__main__":
   main()
