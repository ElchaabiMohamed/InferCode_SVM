def swap_unique_keys_values(in_dict):
    
    dict_out = {}
    not_unique = set()
    for k,v in list(in_dict.items()):
        
        if v in dict_out:
            not_unique.update([v])
            del dict_out[v]
            
        elif v not in not_unique:
            dict_out[v] = k
            
    return dict_out