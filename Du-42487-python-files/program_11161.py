a = []
def swap(a,i,j):
    tmp = a[p]
    a[p] = a[i]
    a[i] = tmp

def reverse(a):
    i = 0 
    while i < len(a) /2:
        swap(a, i, len(a) - i - 1)
    i = i + 1
        

def main():
    print(swap(a,1,2))
    print(reverse(a))

if __name__ == "__main__":
   main()
