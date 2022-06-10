#!/usr/bin/env python

def find_smallest_position(a,i):
   p = i
   j = i + 1
   while j < len(a):
      if a[j] < a[p]:
         p = j
      j = j + 1
   return p

def swap(a,i,p):
   tmp = a[p]
   a[p] = a[i]
   a[i] = tmp

def selection_sort(a):
   i = 0
   while i < len(a):
      p = find_smallest_position(a,i)
      swap(a,i,p)
      i = i + 1

def main():
   a = [99, -500, 60, 2, 4, -20, 600]
   selection_sort(a)
   print(a)

if __name__ == "__main__":
   main()