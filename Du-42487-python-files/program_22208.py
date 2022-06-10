import sys



def swap_keys_values(d):
   e = {}
   for d_tup in list(d.items()):
      if d.values.count(d_tup[1]) == 1:  
         e[d_tup[1]] = d_tup[0]

   return e
