import sys

def swap_unique_keys_values(d):
   d2 = {}
   for (k,v) in list(d.items()):
      if v not in list(d2.values()):
         d2[k] = v
      else:
         del d2[k]
         
   print(d2)
   
   
   d3 = {}
   for (k, v) in list(d2.items()):
      d3[v] = k
   
   return d3
   
def main():
   print((swap_keys_values(d)))
   

if __name__ == '__main__':
   main()