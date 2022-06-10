def swap_keys_values(d):
   reverse = {}
   for k, v in list(d.items()):
      reverse[v] = k
   return reverse

