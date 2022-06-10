import sys 

d = {"a" : 1, "b" : 2, "c" : 3}

def swap_keys_values(x):
   new_d = dict((v,k) for k,v in list(x.items()))
   return (new_d)  

