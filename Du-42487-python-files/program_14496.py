#!/usr/bin/env python3
import sys

def power(m, n):
   if n == 0:
      return 1
   return m * power(m, n-1)

def main():
   print((power(4, 4)))
   
if __name__ == "__main__":
   main()