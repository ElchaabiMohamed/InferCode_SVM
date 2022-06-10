def swap_keys_values():
   a = [v for k, v in list(d.items())]
   return {v:k for k, v in list(d.items())}
