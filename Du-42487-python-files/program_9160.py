def swap_keys_values(d):
    new = ({v: k for k,v in list(d.items())})
    return new
