import sys

def a2l(l1, l2=[]):
   if len(l2) == 0:
      l2 = []
   for i in l1:
      l2.append(i)
   return l2

def main():
   l1 = ["cat", "dog"]
   nlist = a2l(l1)
   print(nlist)

   l2 = ["lion"]
   nlist = a2l(l2, ["antelope"])
   print(nlist)

   l3 = ["fox", "chicken"]
   nlist = a2l(l3)
   print(nlist)

if __name__ == '__main__':
   main()