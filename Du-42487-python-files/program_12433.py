def swap_unique_keys_values(d):
    new_dict = {}
    for key in d:
       if d[key] not in new_dict:
          new_dict[d[key]] = key
    return new_dict
