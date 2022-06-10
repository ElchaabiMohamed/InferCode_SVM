#!/usr/bin/env python

def union(a,b):
   c = []
   c = a - b 
   
   seen = {}
   
   i = 0
   while i < len(c):
      if lines(c) not in seen:
         sys.stdout.write(lines[c])
      i = i + 1

def intersection(a,b):
   c = []
   c = a + b

   seen = {}
   
   i = 0 
   while i < len(c):
      if lines(c) in seen:
         sys.stdout.write(lines[c])
      i = i + 1








