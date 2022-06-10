def reverse(a):
   temp=[]
   i=0
   while i!=len(a):
      temp.append(len(a)-i)
      i=i+1
   a=temp
   return a