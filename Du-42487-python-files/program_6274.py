def swap_key_values(dict_descriptor):
  new_dict = {}
  for keys,values in list(dict_descriptor.items()):
          new_dict[values] = keys
  return(new_dict)
