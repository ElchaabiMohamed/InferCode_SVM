import sys
def selection(a):
   i = 0
   while i < len(a):
      j = i + 1
      p = i
      while j < len(a):
         if a[j] < a[p]:
            p = j
         j += 1
      a[p],a[i] = a[i],a[p]
   i += 1
   return a
