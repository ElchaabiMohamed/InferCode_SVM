def swap_keys_values(d):
    swappedDict = {}
    for i in d:
        swappedDict[d[i]] = i
    return swappedDict


def main():

    a = {
    1: "a",
    2: "b",
    3: "c",
    }
    print((swap_keys_values(a)))

if __name__ == "__main__":
    main()