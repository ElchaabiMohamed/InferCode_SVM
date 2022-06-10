def swap_unique_keys_values(d):
    values = []
    for key in d:
       values.append(key)
    for value in values:
       if count(value) < 2:
          unique_values.append(value)
    for key in d:
       if key in unique_values:
          new_dict[key[unique_values]] = key
    return new_dict
