import sys

def minimum(l):
   biggest = l[0]
   for c in l:
      if c < biggest:
         biggest = c
   return biggest

def main():
    min = None
    print((minimum([6,5,1,3,4])))
    print((minimum([6,5,11,3,4])))
    print((minimum([6,15,11,13,14])))
    print((minimum([6,15,11,13,4])))

if __name__ == '__main__':
    main()