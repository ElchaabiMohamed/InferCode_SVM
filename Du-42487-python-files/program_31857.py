def swap_unique_keys_values(d):
   new_dict = {value: key for (key, value) in list(d.items()) if value not in new_dict}
   return new_dict