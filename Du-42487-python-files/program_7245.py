import sys
my_dict = {'a' : 4, 'b' : 7, 'c' : 10}
def swap_key_values(d):
   d = {v:k for (k,v) in list(d.items())}
   return d

def main():
   d = my_dict
   new_dict = swap_key_values(d)
   print(new_dict)

if __name__ == '__main__':
   main()