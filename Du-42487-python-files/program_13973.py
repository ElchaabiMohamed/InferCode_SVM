def swap_unique_keys_values(d):
   d1={}
   d2={}
   unique=[]
   for k in list(d.keys()):
      if k in d1:
         d1[k]+=1
      else:
         d1[k]=1
   for (k,v) in list(d.items()):
      if d1[k]==1:
         d2[v]=k
      else:
         continue

   return (d2)
