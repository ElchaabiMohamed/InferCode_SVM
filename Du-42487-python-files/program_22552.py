import sys


def reverse_list(l):
   l2 = []
   i = 0
   while l:
      l2.append(l[len(l) -i -1])
      tmp = l.pop()
   return l2





def main():
    print((reverse_list([1,2,3])))
    print((reverse_list([3,4,5,6])))
    print((reverse_list([1,2])))

if __name__ == '__main__':
    main()
