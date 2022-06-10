a = []
def swap(a,i,j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp
    return a
def reverse(a):
    i = len(a)-1
    j = 0
    while i >= 0 and j < len(a) and j != i:
       swap(a,i,j) 
       i = i - 1
       j = j + 1
    return a
def main():
    print(swap(5,9,4))
    print(reverse(5,9,4))

if __name__ == "__main__":
   main()
