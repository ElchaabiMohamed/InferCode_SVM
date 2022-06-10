from sortedcontainers import SortedDict

def swap_keys_values(d):
    d = dict((v,k) for k,v in list(d.items()))
    d = SortedDict(d)
    print((d.items))
