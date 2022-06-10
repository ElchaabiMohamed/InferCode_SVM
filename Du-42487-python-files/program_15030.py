import sys
def swap_keys_values(d):
  new_dict={}
  for (k) in d:
    new_dict[d[k]]=k 
  return new_dict
