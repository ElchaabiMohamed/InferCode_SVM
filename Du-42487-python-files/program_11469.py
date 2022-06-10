def swap_unique_keys_values(d):
   tempd = {}
   tempd = {k:v for (k,v) in list(d.items()) if v.count(v) < 2}

   new_dict = {v:k for (k,v) in list(tempd.items())}
   return new_dict

if __name__ == "__main__":
   main()