import sys

a = []
b = []
c = []

s = sys.stdin.readlines()
line = s[0]
a = line.split()

line = s[1]
b = line.split()

i = 0
while i < len(a):
   if a[i] not in b:
      c.append(a[i])
   i += 1
   
   
print("Removing elements of " + str(b) + " from " + str(a))
print(c)