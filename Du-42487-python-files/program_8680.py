

def swap_unique_keys_values(d):
    kv = []
    values = []
    dic = {}
    new_values = []
    new_keys = []
    seen={}

    for k, v in list(d.items()):
        kv.append((v, k))

    seen[kv[0][0]] = False

    for t in kv:
        if t[0] not in seen:
            seen[t[0]] = False
        else:
            seen[t[0]] = True

    for t in kv:
        if seen[t[0]] == False:
            dic[t[0]] = t[1]

    return dic