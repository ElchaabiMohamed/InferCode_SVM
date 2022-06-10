def swap_keys_values(d):
   new_dict = {}
   for pair in list(d.items()):
      new_dict[pair[1]] = pair[0]
   return new_dict

def main():
   print((swap_keys_values(my_dict)))

if __name__ == '__main__':
   main()