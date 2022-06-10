def swap_unique_keys_values(d):
   m = {}
   for i in list(d.items()):
      if i[1].count(d) == 1:
         m[i[1]] = i[0]
   return m