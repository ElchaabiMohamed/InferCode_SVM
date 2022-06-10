import sys
def reverse(a, i):
   i = 0
   lines = sys.stdin.readlines()
   while i < len(a):
      print((lines[i] - 1 - i))
   i = i + 1
   return a