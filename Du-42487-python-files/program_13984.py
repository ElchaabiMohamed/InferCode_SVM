import sys

d = {
'hey': 3,
'yo': 4
}

def swap_key_values(d):
   e = {}
   for d_tup in list(d.items()):
      e[d_tup[1]] = d_tup[0]

   return e


print((swap_key_values(d)))