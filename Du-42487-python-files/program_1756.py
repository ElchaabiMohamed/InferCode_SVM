import sys
def swap_unique_keys_values(x):
  new = {}
  for k in x:
    c = x.get(k)
    if c in new:
      del new[c]
    else:
      new[c] = k
  return(new)

def main():
  x = {'a' : 4, 'b' : 7, 'c' : 10, 'd' : 7}
  print((swap_unique_keys_values(x)))
if '__name__' == '__main__':
  main()
