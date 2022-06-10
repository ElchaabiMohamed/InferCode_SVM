import sys
def swap_unique_keys_values(d):
  new_dict={}
  a=[]
  for v in list(d.values()):
    a.append(v)
  for k in d:
    if a.count(d[k])==1:
      new_dict[d[k]]=k 
  return new_dict
