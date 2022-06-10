#!/usr/bin/env python

def union(a,b):
   i = 0
   while i < len(a) and a[i] != b:
      i = i + 1
   return i < len(a)

lines = sys.stdin.readlines()
seen = []

i = 0
while i < len(lines):
   if not union(seen, lines[i]):
      sys.stdout.write(lines[i])
      seen.append(lines[i])
   i = i + 1


   
