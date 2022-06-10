import sys

def swap_unique_keys_values(d):
    new_dict = print(sorted(dict([(v,k) for k,v in d.items() if list(d.values()).count(v) == 1 ])))
