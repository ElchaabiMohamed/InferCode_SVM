import sys
def unique(x):
  new = {}
  for k in x:
    c = x.get(k)
    if c in new:
      del new[v]
    else:
      new[v] = k
  return(new)

def main():
  x = {'a' : 4, 'b' : 7, 'c' : 10, 'd' : 7}
  print((unique(x)))
if '__name__' == '__main__':
  main()
