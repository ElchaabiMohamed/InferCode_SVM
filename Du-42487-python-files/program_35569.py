def swap_unique_keys_values(d):
    new_dict = {}
    unique_values = []
    values = []
    for key in d:
       values.append(key)
    for value in values:
       if values.count(value) < 2:
          unique_values.append(value)
    for key in d:
       if key in unique_values:
          new_dict[unique_values[key]] = key
    return new_dict
