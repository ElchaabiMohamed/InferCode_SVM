import sys

def swap_keys_values(d):
   swapped = {}
   for (k, v) in list(d.items()):
      swapped[v] = k

   return swapped

if __name__ == "__main__":
   main()