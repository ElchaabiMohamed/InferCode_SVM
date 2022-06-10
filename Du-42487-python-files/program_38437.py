#!/usr/bin/env pyhton3


def sumup(n):
   if n == 1:
      return 1
   return (n + sumup(n-1))

def main():
   pass

if __name__ == "__main__":
   main()
