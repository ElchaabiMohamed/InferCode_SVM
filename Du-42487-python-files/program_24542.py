#review section
def union(a,b):
 set = {} #variable name message read etc.
 
 i = 0
 while i < len(a):
  set[a[i]] = True
  i = i + 1

 j = 0
 while j < len(b):
  if not (b[j] in set):
   set[b[j]] = True
  j = j + 1

 return set

def intersection(a, b):
 set = {}

 i = 0
 while i < len(a):
  if a[i] in b and not (a[i] in set):
   set[a[i]] = True
  i = i + 1

  return set


 

