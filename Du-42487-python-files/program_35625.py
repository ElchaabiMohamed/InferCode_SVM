def swap_unique_keys_values(my_dict):
    new = {}
    seen = []
    unseen = []
    for k,v in list(my_dict.items()):
        if v in unseen:
            seen.append(v)
        else:
            unseen.append(v)
    for k in my_dict:
        if my_dict[k] not in seen and unseen:
            new[my_dict[k]] = k
    return new
