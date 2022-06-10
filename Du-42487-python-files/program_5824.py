import sys
def swap(x):
  x = {v : k for k, v in list(x.items())}
  return x

dict = {'a':4, 'b':7, 'c':10}
dict = list(dict.items())
print (dict)
if '__name__' == '__main__':
  main()
  
