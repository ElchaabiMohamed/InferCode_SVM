import sys



def swap_unique_keys_values(d):
   e = {}
   for d_tup in list(d.items()):
      if list(d.values()).count(d_tup[1]) == 1:  
         e[d_tup[1]] = d_tup[0]

   return e
