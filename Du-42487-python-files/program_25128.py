def swap_unique_keys_values():
    new_dic = {}
    for key in dic:
        if dic[key] not in new_dic:
            new_dic[dic[key]] = key
    return new_dic
