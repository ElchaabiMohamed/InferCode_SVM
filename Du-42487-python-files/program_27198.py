pi = 3.141

def swap(a, i, j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp

def reverse(a):
    i = 0
    j = -1
    while i < len(a) / 2:
        swap(a, i, j)
        i += 1
        j -= 1

def main():
    reverse(a)
    print(a)

if __name__ == "__main__":
   main()