# {'a' : 4, 'b' : 7, 'c' : 10}
#def swap_key_values(in_dict):
  #  out_dict = {}
    # puts keys and values into dictionary

  #  for k, v in in_dict.items:  # .items turns keys and values of in_dict into tuples
   #     out_dict[v] = k

  #  return out_dict

#[(4, 'a'), (7, 'b'), (10, 'c')]

def swap_keys_values(d):
    return dict([(v, k) for k,v in list(d.items())])
