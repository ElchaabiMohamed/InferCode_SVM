def swap_unique_keys_values(d):
   dict = {}
   for k in d:
      v = d.get(k)
      if v in dict:
          del dict[v]
      else:
          dict[v] = k
   return (dict)