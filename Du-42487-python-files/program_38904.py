def swap_unique_keys_values(d):
   keys = list(d.keys())
   values = list(d.values())
   newD = {}
   for i in range(len(keys)):
      if values.count(values[i]) == 1:
         newD[values[i]] = keys[i]
   return newD