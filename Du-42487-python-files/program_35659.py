def swap_unique_keys_values(d):
   new_dict = {}
   for (key, value) in list(d.items()):
      if value not in new_dict:
         new_dict[value] = key
   return new_dict