import sys

def swap_unique_keys_values(d):
    new_d = {}
    for k in d:
        if d[k] not in new_d:
            new_d[d[k]] = k
    return new_d


if __name__ == "__main__":
    print((swap_unique_keys_values({1:"a", 2:"b", 3:"a", 4:"d"})))