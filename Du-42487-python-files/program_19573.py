import sys

#d = {'a' : 4,
#     'b' : 7,
 #    'c' : 10}


def swap_keys_values(d):
   a = []
   for entry in list(d.items()):
      u = entry[::-1]
      a.append(u)
   return a

#print(swap_keys_values(d))
