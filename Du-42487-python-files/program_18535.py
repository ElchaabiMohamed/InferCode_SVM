import sys

def swap_keys_values(d):
   newdict = {}
   keys = list(d.keys())
   values = list(d.values())
   i = 0
   while i < len(d.keys):
      newdict[keys[i]] = values[i]
      i = i + 1
   return newdict