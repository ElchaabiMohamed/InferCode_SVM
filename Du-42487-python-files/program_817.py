def swap_unique_keys_values(d):
   keys = list(d.keys())
   values = list(d.values())
   newD = {}
   for i in range(len(keys)):
      if values.count(values[i]) == 1:
         newD[keys[i]] = values[i]
   return newD