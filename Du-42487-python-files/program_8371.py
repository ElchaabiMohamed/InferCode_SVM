import sys

def swap_keys_values(d):
   d2 = {}
   for (k, v) in list(d.items()):
      d2[v] = k
   
   return d2
   
def main():
   print((swap_keys_values(d)))
   

if __name__ == '__main__':
   main()