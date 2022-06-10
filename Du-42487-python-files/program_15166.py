my_dict = {'a': 4, 'b': 7, 'c': 10}

def swap_key_values(my_dict):
   return {v : k for k, v in list(my_dict.items())}


print((swap_key_values(my_dict)))