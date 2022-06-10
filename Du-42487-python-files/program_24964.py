def reverse(a):
   temp=[]
   i=0
   while i!=len(a):
      temp.append(a[len(a)-i-1])
      i=i+1
   a=temp
   return a