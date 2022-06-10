def swap_unique_keys_values(d):
    e = {}
    for left, right in d:
        if right not in e:
           e[left] = right

    return {v: k for k, v in list(e.items())}


