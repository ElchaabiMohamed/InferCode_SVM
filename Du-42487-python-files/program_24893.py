def swap_unique_keys_values(d):
   tempd = {}
   for (k,v) in list(d.items()):
      if v.count(str(v)) < 2:
         tempd = {k : v}

   new_dict = {v:k for (k,v) in list(tempd.items())}
   return new_dict

if __name__ == "__main__":
   main()