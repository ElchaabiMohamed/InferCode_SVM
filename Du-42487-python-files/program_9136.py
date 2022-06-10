import sys

def swap_keys_values(d):
    print(d)
    new_dict = {}
    print((list(d.keys())))
    print((list(d.items())))
    print((list(d.values())))
    for k, v in list(d.items()):
        new_dict[v] = k
    return new_dict

dicti = {
    "b" : 7,
    "c" : 10,
    "a" : 4
}

print((swap_keys_values(dicti)))