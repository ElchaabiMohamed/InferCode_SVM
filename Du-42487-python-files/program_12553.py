#!/usr/bin/env python

def swap(a,i,j):
   tmp = a[i]
   a[i] = a[j]
   a[j] = tmp

def selection_sort(a):
   i = 0
   while i < len(a):
      j = i + 1
      while j < len(a):
         if a[j] < a[i]:
            swap(a,i,j)
         j = j + 1
      i = i + 1
   return a

def main():
   a = [1,2,3,1,2,3]
   print(selection_sort(a))

if __name__ == "__main__":
   main()
