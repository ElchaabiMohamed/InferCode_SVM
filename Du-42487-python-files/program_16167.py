def union(f1con,f2con):
#Accepts exactly two list arguments, and returns a new list containing elements which occur in either list, and no duplicates.
   import sys
   d1={}
   i=0
   while i!=len(f1con):
      line=f1con[i].rstrip()
      d1[line]=True
      i=i+1
   dups=[]
   i=0
   while i!=len(f2con):
      line=f2con[i].rstrip()
      if line in list(d1.keys()):
         dups.append(line)
      i=i+1
   
   dups=sorted(list(set(dups)))
   
   return dups

def intersection():
#Accepts exactly two list arguments, and returns a new list containing elements which occur in both list, and no duplicates. 
   import sys
   d1={}
   i=0
   while i!=len(f1con):
      line=f1con[i].rstrip()
      d1[line]=True
      i=i+1
   dups=[]
   i=0
   while i!=len(f2con):
      line=f2con[i].rstrip()
      if line in list(d1.keys()):
         dups.append(line)
      i=i+1
   
   dups=sorted(list(set(dups)))
   
   return dups

