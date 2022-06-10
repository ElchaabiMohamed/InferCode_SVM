def swap_keys_values(d):
   m = {}
   for i in list(d.items()):
      m[i[1]] = i[0]
   return m