dictionary = {'a': 4, 'b': 7, 'c': 10}

def swap_keys_values(d):
    d = dict((v, k) for k, v in list(d.items()))
    new_dict = sorted(list(d.items()), key=lambda t: t[0])
    print(new_dict)

#swap_keys_values(dictionary)
