def swap_key_values(my_dict):
   return {v:k for (k,v) in list(my_dict.items())}

def main():
   new_dict = swap_key_values(my_dict = {"a": 4, "b": 7, "c": 10})
   print(new_dict)

if __name__ == '__main__':
   main()