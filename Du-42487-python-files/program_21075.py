#!/usr/bin/env pyhton3


def maximum(a):
   minim = None
   if len(a) == 1:
      return a[0]
   newmax = maximum(a[1:])
   if a[0] > newmax:
      return a[0]
   else:
      return newmax
   

def main():
    min = None
    print((maximum([6,5,1,3,4])))
    print((maximum([6,5,11,3,4])))
    print((maximum([6,15,11,13,14])))
    print((maximum([6,15,11,13,4])))

if __name__ == '__main__':
    main()

