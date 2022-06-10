import sys

def swap_unique_key_values(d):
   new_d = {}
   for (k,v) in list(d.items()):
     if not v in new_d:
        new_d[v] = k
     else:
        del new_d[v]
   return new_d
   




