#!/usr/bin/env pyhton3


def minimum(a):
   minim = None
   if len(a) == 1:
      return a[0]
   newm = minimum(a[1:])
   if a[0] < newm:
      return a[0]
   else:
      return newm
   

def main():
    min = None
    print((minimum([6,5,1,3,4])))
    print((minimum([6,5,11,3,4])))
    print((minimum([6,15,11,13,14])))
    print((minimum([6,15,11,13,4])))

if __name__ == '__main__':
    main()

