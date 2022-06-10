import sys
my_dict = {'a' : 4, 'b' : 7, 'c' : 10, 'd' : 7}
def swap_unique_keys_values(d):
   d = {v:k for (k,v) in list(d.items())}
   return d

def main():
   newd = {}
   d = my_dict
   new_dict = swap_unique_keys_values(d)
   
   for k, v in list(new_dict.items()):
      if v not in list(newd.values()):
         newd[k] = v
   print(newd)

if __name__ == '__main__':
   main()
