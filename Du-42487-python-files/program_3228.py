from collections import Counter

def swap_keys_values(d):
    l = Counter(list(d.values()))
    return {value: key for key,value in list(d.items())
            if l[value] == 1}

