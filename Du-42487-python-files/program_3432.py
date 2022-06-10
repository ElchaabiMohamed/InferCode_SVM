import sys

def swap_unique_keys_values(d):
   new_d = {}
   a = []
   for value in list(d.values()):
         a.append(value)
   for key in d:
      if a.count(d[key]) == 1:
         new_d[d[key]] = key
   return(new_d)
