def swap_unique_keys_values(d):
   return({v : k for (k, v) in list(d.items()) if v not in list(d.keys())})

def main():
   return(swap_unique_keys_values(d))

if __name__ == '__main__':
   main()