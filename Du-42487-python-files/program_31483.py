def swap_key_values(d):
   d = {}
   return {v:k for (k,v) in list(d.items())}

def main():
   new_dict = swap_key_values(my_dict)

if __name__ == '__main__':
   main()