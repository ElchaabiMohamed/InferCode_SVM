import sys

def swap_keys_values(d):
   a = []
   d_2 = {}
   for entry in list(d.items()):
      swap = entry[::-1]
      a.append(swap)
   for k, v in a:
      d_2[k] = v
   return d_2
