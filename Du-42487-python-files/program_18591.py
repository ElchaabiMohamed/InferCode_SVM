import sys

def swap_unique_keys_values(d):
   a = []
   d_2 = {}
   for entry in list(d.items()):
      swap = entry[::-1]
      a.append(swap)
   for k, v in a:
      d_2[k] = v
   return d_2

def main():
   d = {'a' : 4,
        'b' : 7,
        'c' : 10,
        'd' : 7}
   print((swap_unique_keys_values(d)))

if __name__ == '__main__':
   main()
