import sys

def swap_unique_keys_values(my_dict):
  d = {}
  for key in my_dict:
     value = my_dict.get(k)
     if value in d:
         del d[v]
     else:
         d[v] = k
  return (d)
