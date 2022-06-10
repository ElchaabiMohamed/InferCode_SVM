import sys

def swap(a,i,j):
   tmp = a[i]
   a[i] = a[j]
   a[j] = tmp

def reverse(a):
   x = 0
   y = len(a)
   z = len(a) / 2

   while x < y:
      swap(x,y)
      x = x + 1
      y = y - 1
