import sys

def swap_unique_keys_values(d):
   d2 = {}
   d3 = {}
   ds = sorted(list(d.items()), reverse = True)
   print(ds)
   for k, v in ds:
      if v not in d2:
         d2[v] = k
      else:
         d2[v] = 'X'
   print(d2)
   ds2 = sorted(list(d2.items()), reverse = True)
   print(ds2)
   for k, v in ds2:
      if v != 'X':
         d3[k] = v
   return d3   

