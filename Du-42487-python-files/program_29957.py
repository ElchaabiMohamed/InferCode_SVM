import sys
my_dict = {'a' : 4, 'b' : 7, 'c' : 10}
def swap_keys_values(d):
   d = {v:k for (k,v) in list(d.items())}
   return d

def main():
   d = my_dict
   new_dict = swap_keys_values(d)
   n = set(new_dict)
   print(n)

if __name__ == '__main__':
   main()