#!/use/bin/env python

def swap(a,i,j):
   tmp = a[j]
   a[j] = a[i]
   a[i] = tmp
   return a

def reverse(a):
    a.reverse()

    return a

def main():

    a = [4, 3, 1, 2]

    print(swap(a,2,3))
    print(reverse(a))


if __name__ == "__main__":
    main()

        
        

