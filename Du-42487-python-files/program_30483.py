import sys

def swap_keys_values(d):
   new_d = {}
   for key in d:
      new_d[d[key]] = key
   return(new_d)
