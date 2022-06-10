#!/usr/bin/env python3
import sys

def fibonacci(n):
   if n == 0:
      return 1
   elif n < 0:
      return 0
   return fibonacci(n - 1) + fibonacci(n - 2)
   

def main():
   print((fibonacci(0)))
   
if __name__ == "__main__":
   main()