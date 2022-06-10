import sys

def swap_unique_keys_values(d):
   seen = []
   unseen = []
   for v in list(d.keys()):
      va = d[v]
      if va in unseen:
         seen.append(va)
      else:
         unseen.append(va)
      out = {v:k for k,v in list(d.items()) if v not in seen}
   return out