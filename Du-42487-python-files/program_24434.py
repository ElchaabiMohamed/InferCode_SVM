def swap_unique_keys_values(dic):
    new_dic = {}
    for key in dic:
        if dic[key] not in new_dic:
            new_dic[dic[key]] = key
        else:
            del new_dic[dic[key]]
    return new_dic
