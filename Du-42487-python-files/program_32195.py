import sys
def swap(x):
  new = {v : k for k, v in list(x.items())}
  return (new)

def main():
  x = {'a':4, 'b':7, 'c':10}
  print((swap(x)))

if '__name__' == '__main__':
  main()
  
