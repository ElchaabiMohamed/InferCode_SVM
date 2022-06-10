import sys

def swap_keys_values(d):
   a = []
   for entry in list(d.items()):
      u = entry[::-1]
      a.append(u)
   return a



if __name__ == '__swap_keys_values__':
   swap_keys_values(d)
