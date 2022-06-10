def swap_unique_keys_values(in_dict):
    
    out_dict = {}
    blist = set()
    for k,t in list(in_dict.items()):
        
        if t in out_dict:
            blist.update([t])
            del out_dict[t]
            
        elif t not in blist:
            out_dict[v] = k
            

    return out_dict