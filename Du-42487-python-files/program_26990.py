#!/usr/bin/env python3
import sys

def sumup(n):
   if n == 0:
      return 0
   
   return n + sumup(n - 1)

def main():
   print((sumup(2)))
   
if __name__ == "__main__":
   main()