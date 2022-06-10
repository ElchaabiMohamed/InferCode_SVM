def swap_keys_values(d):
   newD = {}
   for (k, v) in list(d.items()):
      newD[v] = k
   return newD