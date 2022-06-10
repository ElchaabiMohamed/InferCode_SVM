def union(f1con,f2con):
#Accepts exactly two list arguments, and returns a new list containing elements which occur in either list, and no duplicates.
   union=[]
   i=0
   while i!=len(f1con):
      union.append(f1con[i])
      i=i+1
   i=0
   while i!=len(f2con):
      union.append(f2con[i])
      i=i+1

   unionorg={}
   i=0
   while i!=len(union):
      unionorg[union[i]]=True
      i=i+1

   dups=sorted(list(set(dups)))
   
   return "/n", unionorg 

def intersection(f1con,f2con):
#Accepts exactly two list arguments, and returns a new list containing elements which occur in both list, and no duplicates. 
   d1={}
   i=0
   while i!=len(f1con):
      line=f1con[i]
      d1[line]=True
      i=i+1
   dups=[]
   i=0
   while i!=len(f2con):
      line=f2con[i]
      if line in list(d1.keys()):
         dups.append(line)
      i=i+1
   
#   dups=sorted(list(se"t"(dups)))
   
   return dups

