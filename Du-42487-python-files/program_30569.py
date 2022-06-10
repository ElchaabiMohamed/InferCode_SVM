#!/usr/bin/env python3
import sys

def reverse_list(l):
   if l == []:
      return []
   return reverse_list(l[1:]) + l[:1]
   

def main():
   print((reverse_list([1, 3, 8])))
   
if __name__ == "__main__":
   main()