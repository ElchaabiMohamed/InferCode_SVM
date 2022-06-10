import sys

a = sys.stdin.readlines()
b = sys.stdin.readlines()

def union(a, b):
	i = 0
	while i < len(a) and a[i] != v:
		i = i + 1

	return i < len(a)

lines = sys.stdin.readlines()
seen = []

i = 0
while i < len(lines):
   if not is_in(seen, lines[i]):    
      sys.stdout.write(lines[i])
      seen.append(lines[i])
   i = i + 1
