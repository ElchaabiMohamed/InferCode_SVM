def swap_unique_keys_values(d):
   m = {}
   for i in list(d.items()):
      if list(d.values()).count(i[1]) == 1:
         m[i[1]] = i[0]
   return(m)
