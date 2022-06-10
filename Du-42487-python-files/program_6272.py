import sys
my_dict = {'a' : 4, 'b' : 7, 'c' : 10}

def swap_keys_values(d):
   new_dict = {v:k for (k,v) in list(d.items())}
   print((sorted(new_dict.items())))
def main():
   new_dict = swap_keys_values(my_dict)

if __name__ == "__main__":
   main()
