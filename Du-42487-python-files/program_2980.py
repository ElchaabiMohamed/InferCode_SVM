def swap_unique_keys_values(d):
   d1={}
   d2={}
   unique=[]
   for v in list(d.values()):
      if v in d1:
         d1[v]+=1
      else:
         d1[v]=1
   for (k,v) in list(d.items()):
      if d1[v]==1:
         d2[v]=k
      else:
         continue

   return (d2)
