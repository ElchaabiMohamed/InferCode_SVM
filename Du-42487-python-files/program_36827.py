#!/usr/bin/env pyhton3


def factorial(n):
   if n == 0 or n == 1:
      return 1
   return n * factorial(n-1)

def main():
   print((factorial(4)))

if __name__ == "__main__":
   main()
