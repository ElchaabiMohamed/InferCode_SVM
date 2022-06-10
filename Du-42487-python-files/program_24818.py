import sys

def swap_keys_values(d):
   new_d = d((v,k) for k,v in list(d.items()))
   return (new_d)

def main():
   d = {"a" : 1, "b" : 2, "c" : 3}
   print((swap_keys_values(d)))

if __name__ == "__main__":
   main()