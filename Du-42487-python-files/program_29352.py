import collections

def swap_keys_values(d):
    d = dict((v,k) for k,v in list(d.items()))
    d = collections.OrderedDict(sorted(list(d.items()), key=lambda t: t[0]))
    print(d)
