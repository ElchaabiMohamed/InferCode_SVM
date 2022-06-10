
def swap(a,i,j):
    tmp = a[j]
    a[j] = a[i]
    a[i] = tmp

def reverse(a):
    b = 0
    while b < (len(a)/2):
        swap(a,b,len(a) - b - 1)
        b += 1
    return a


def main():
    a = [4, 3, 1, 2]
    swap(a,2,3)
    reverse(a)
    print(a)
    

if __name__ == "__main__":
   main()