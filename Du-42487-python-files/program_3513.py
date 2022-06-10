import sys

def swap_keys_values(d):
   new_d = {}
   for key in d:
      if list(d.values()).count(d[key]) == 1:
         new_d[d[key]] = key
   return(new_d)
