import sys
def swap(x):
  x = {v : k for k, v in list(x.items())}
  return x

dict = {'a':4, 'b':7, 'c':10}
n = swap(dict)
n = list(n.items())
print (n)
if '__name__' == '__main__':
  main()
  
