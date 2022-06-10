import sys


def swap_keys_values(my_dict):
   new_dict = dict((v,k) for k,v in list(my_dict.items()))
   return (new_dict)

def main():
   d = {'a' : 4, 'b' : 7, 'c' : 10}
   print((swap_keys_values(my_dict)))


if __name__ == "__main__":
  main()

