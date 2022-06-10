#!/usr/bin/env python
pi = 3.141

def circumfrence(r):
   cir = 2 * pi * r
   return cir

def area(r):
   ar = pi * r ** 2
   return ar


def main():
   print(circumfrence(5))
   print(area(10))

if __name__ == "__main__":
   main()
