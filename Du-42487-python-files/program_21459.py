import sys
lines = sys.stdin.readlines()

def f(n):
   i = 2
   while i < n and n % i != 0:
      i = i + 1
   
   return i == n

i = 0
while i < len (lines):
   if f ( int (lines[i])):
      sys.stdout.write(lines[i])
   i = i + 1
