my_dict = {'a' : 4, 'b' : 7, 'c' : 10}

def swap_unique_keys_values(d):
   new_dict = {}
   for pair in list(d.items()):
      if pair[1] not in new_dict:
         new_dict[pair[1]] = pair[0]
   return new_dict

def main():
   print((swap_unique_keys_values(my_dict)))

if __name__ == '__main__':
   main()