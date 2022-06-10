def swap_keys_values(d):
   tempd = {}
   {tempd[list(d.keys())] for item in d if d.count(list(d.values())) < 2}

   new_dict = {v:k for (k,v) in list(tempd.items())}
   return new_dict

if __name__ == "__main__":
   main()