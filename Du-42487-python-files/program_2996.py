#!/usr/bin/env pyhton3


def reverse_list(a):
   if len(a) == 0:
      return []
   elif len(a) == 1:
      return [a[0]]
   return reverse_list(a[1:]) + [a[0]]

def main():
    print((reverse_list([1,2,3])))
    print((reverse_list([3,4,5,6])))
    print((reverse_list([1,2])))
    print((reverse_list([])))

if __name__ == '__main__':
    main()

