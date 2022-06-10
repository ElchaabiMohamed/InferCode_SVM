#!/usr/bin/env python

total = 0 
n = eval(input()) 

i = 0
while i < 10:
   total = total + (i + 1) 
   print(i % 2)
   i = i + 1

print(total) 
