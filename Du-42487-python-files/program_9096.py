import sys

def swap(a,i,j):
  tmp = a[i]
  a[i] = a[j]
  a[j] = tmp
  return a

def reverse(a):
   i = 0
   while i < len(a)/2:
      swap(a,a[i],a[len(a)-i-1])
   return a


