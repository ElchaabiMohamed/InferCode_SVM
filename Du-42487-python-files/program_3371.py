#!usr/bin/env python3


def swap_unique_keys_values(d):
    return {t[1]: t[0] for t in list(d.items()) if list(d.values()).count(t[1]) == 1}
