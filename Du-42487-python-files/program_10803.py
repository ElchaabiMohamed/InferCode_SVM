import sys

def is_in(a,v):
   i = 0
   while i < len(a) and a[i] != v:
      i = i + 1

   return i < len(a)

lines = sys.stdin.readlines()
seen = []

i = 0
while i < len(lines):
   if not is_in(seen, lines[i]):    # <-- We use the "is_in" function.
      sys.stdout.write(lines[i])
      seen.append(lines[i])
   i = i + 1
