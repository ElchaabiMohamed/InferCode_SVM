import sys

def swap_unique_keys_values(d):
    new_d = {}
    values = list(d.values())
    keys = list(d.keys())
    i = 0
    for i in range(0, len(values)):
        if values.count(values[i]) < 2:
            new_d[values[i]] = keys[i]
    return new_d

def main():
    print((swap_unique_keys_values({1:"a", 2:"b", 3:"a", 4:"d"})))

if __name__ == "__main__":
    main()
