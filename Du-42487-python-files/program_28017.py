import sys



def swap_keys_values(d):
   e = {}
   for d_tup in list(d.items()):
      e[d_tup[1]] = d_tup[0]

   return e
