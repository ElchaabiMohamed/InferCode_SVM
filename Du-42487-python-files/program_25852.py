#!/usr/bin/env python

#import func_reverse

def selection_sort(a):
    i = 0
    while i < len(a):
        j = i
        while j < len(a):
            if a[i] > a[j]:
                tmp = a[i]
                a[i] = a[j]
                a[j] = tmp
#                func_reverse.swap(a , i , j)
            j += 1
        i += 1

        return a

def main():

    a = [1, 2, 3, 1, 2, 3]
    print(selection_sort(a))

if __name__ == "__main__":
    main()
