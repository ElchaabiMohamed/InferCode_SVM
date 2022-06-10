#!/usr/bin/env python3
import sys

def count_letters(s):
   if not s:
      return 0
   return 1 + count_letters(s[:-1])
   

def main():
   print((count_letters("")))
   
if __name__ == "__main__":
   main()