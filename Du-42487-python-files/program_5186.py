import sys

def swap(a,i,j):
  tmp = a[j]
  a[j] = a[i]
  a[i] = tmp
  return a

def reverse(a):
   i = 0
   while i < len(a)/2:
      swap(a,a[i],a[len(a)-i-1])
   return a


