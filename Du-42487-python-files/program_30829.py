def reverse(a):
   import sys
   a=sys.stdin.readlines()
   i=0
   b=[]
   while i<len(a):
      f=a[len(a)-i-1]
      i=i+1
      b.append(f.rstrip())
   print(b)
   return a
   
 