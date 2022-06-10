#!/usr/bin/env python
n = 10

i = 0
while i < n:
   if i % 2 == 0 and i < 10:
      i = 0
   elif i % 2 == 1 and i < 10:
      i = 1
   print(i)
   i = i + 1
