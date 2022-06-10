import sys

def swap_keys_values(d):
   d_2 = []
   for entry in list(d.items()):
      u = entry[::-1]
      for k, v in u.split(','):
         d_2[k] = v
   return d_2



if __name__ == '__swap_keys_values__':
   swap_keys_values(d)
