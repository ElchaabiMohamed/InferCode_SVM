#!/usr/bin/env python3
import sys

def factorial(n):
   if n <= 1:
      return 1
   
   return n * factorial(n - 1)

def main():
   print((factorial(1)))
   
if __name__ == "__main__":
   main()