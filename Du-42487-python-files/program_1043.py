# {'a' : 4, 'b' : 7, 'c' : 10}

#[(4, 'a'), (7, 'b'), (10, 'c')]

def swap_keys_values(d):
    return dict([(v, k) for k, v in list(d.items())])
