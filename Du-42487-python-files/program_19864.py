#!usr/bin/python

def swap(a,i,j):
    tmp = a[j]
    a[j] = a[i]
    a[i] = tmp

def smallest_position(a,i):
    p = i
    j = i + 1
    while j < len(a):
        if a[j] < a[p]:
            p = j
        j = j + 1
    return p

def selection_sort(a):
    i = 0
    while i < len(a):
        p = smallest(a,i)
        swap(a,i,p)
        i = i + 1

if __name__ == "__swap__":
    swap(a,1,2)

if __name__ == "__smallest_position__":
    smallest_position(a,1,2)

if __name__ == "__selection_sort__":
    selection_sort(a)