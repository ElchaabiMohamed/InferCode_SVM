import sys
def swap_unique_keys_values(d):
   new_dict = {}
   for k in d:
      v = d[k]
      if v not in new_dict:
         new_dict[v] = k
      else:
         del new_dict[v]
      return new_dict
