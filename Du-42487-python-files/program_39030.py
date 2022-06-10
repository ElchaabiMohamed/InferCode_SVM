def swap_unique_keys_values(dict_descriptor):
  new_dict = {}
  addthosevalues = set()
  for keys,values in list(dict_descriptor.items()):
          if values in new_dict:
                  addthosevalues.update([values])
                  del new_dict[values]
          elif values not in new_dict:
                  new_dict[values] = keys

  return(new_dict)  
