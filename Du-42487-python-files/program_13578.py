def swap_unique_keys_values(d):
   m = {}
   for i in list(d.items()):
      if i[1] not in m:
         m[i[1]] = i[0]
   return m