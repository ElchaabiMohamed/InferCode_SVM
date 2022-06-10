def swap_unique_keys_values(d):
    keyval = []
    new = {}
    done = {}
    for (k, v) in list(d.items()):
        keyval.append((v, k))

    done[keyval[0][0]] = False

    for each in keyval:
        if each[0] not in done:
            done[each[[0]]] = False
        else:
            done[each[0]] = True

        for each in kv:
            if not done[each[0]]:
                new[each[0]] = each[1]

        return new