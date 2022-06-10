def swap_keys_values(x):
   d = {}
   for k, v in list(x.items()):
      d[v] = k
   return(d)
