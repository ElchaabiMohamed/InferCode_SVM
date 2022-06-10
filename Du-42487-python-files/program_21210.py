import sys

def swap_unique_keys_values(my_dict):
  d = {}
  for key in my_dict:
     value = my_dict.get(key)
     if value in d:
         del d[value]
     else:
         d[value] = key
  return (d)
