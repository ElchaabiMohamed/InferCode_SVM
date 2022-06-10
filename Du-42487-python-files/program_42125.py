import sys

def swap(a,i,j):
   tmp = a[i]
   a[i] = a[j]
   a[j] = tmp

def reverse(a):
   x = 0
   y = len(a)

   while x < len(a):
      swap(a,x,y)
      x = x + 1
      y = y - 1
