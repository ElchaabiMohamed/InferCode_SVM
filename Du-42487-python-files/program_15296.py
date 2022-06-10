import sys

def swap_keys_values(d):
   swap1 = {}
   swap2 = {}
   swapsorted = sorted(list(d.items()), reverse = True)
   for k,v in swapsorted:
      swap1[v] = k
   
   swapsorted2 = sorted(list(swap1.items()), reverse = True)
   for k,v in swapsorted2:
      swap2[k] = v
   return swap2