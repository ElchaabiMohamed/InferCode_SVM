import sys
#def main():
#d = { "cat" : 2,
    ##  "dog" : 7,
    #  "horse" : 9,
     # "whale" : 14,}

def swap_keys_values(d):
    d = { "cat" : 2,
      "dog" : 7,
      "horse" : 9,
      "whale" : 14,}

    for key, value in d:
        {value : key for (key, value) in list(d.items())}
    print((swap_keys_values(d)))
