def swap_keys_values(d):
   a = [v for k, v in list(d.items())]
   return {v:k for k, v in list(d.items())}
