import sys
import string

d = {"a": 4, "b": 7, "c": 10, "d" : 7}

def swap_unique_keys_values(d):
   return dict([(v,k) for (k,v) in list(d.items()) if list (d.values()).count(v) ==1])

