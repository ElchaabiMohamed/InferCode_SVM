import sys

def swap_unique_keys_values(d):
   d2 = {}
   d3 = {}
   for (k, v) in list(d.items()):
      if v not in d2:
         d2[v] = k
      else:
         d2[v] = "X"
   
   for (k, v) in list(d2.items()):
      if v != "X":
         d3[k] = v
   
   
   return d3
   
def main():
   print((swap_keys_values(d)))
   

if __name__ == '__main__':
   main()