#!/usr/bin/env python

def union(a,b):
   da = {}
   db = {}

   i = 0
   while i < len(a):
      da[a[i]] = True
      i = i + 1

   i = 0
   while i < len(b):
      db[b[i]] = True
      i = i + 1

   c = []
   for key in da:
      c.append(key)

   for key in db:
      if key not in da:
         c.append(key)

   return c

def intersection(a,b):
   da = {}
   db = {}

   i = 0
   while i < len(a):
      da[a[i]] = True
      i = i + 1

   i = 0
   while i < len(b):
      db[b[i]] = True
      i = i + 1

   c = []
   for key in da:
      if key in db:
         c.append(key)

   return c

if __name__ == "__main__":
   a = [1,2,3,4]
   b = [3,4,5,6]
   print(union(a,b))
   print(intersection(a,b))
