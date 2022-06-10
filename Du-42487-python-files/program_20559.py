import sys
def swap_keys_values(x):
  new = {v : k for k, v in list(x.items())}
  return (new)

def main():
  x = {'a':4, 'b':7, 'c':10}
  print((swap_keys_values(x)))

if '__name__' == '__main__':
  main()
  
