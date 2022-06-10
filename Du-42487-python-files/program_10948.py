#!/usr/bin/env python3
import sys

def reverse_list(l):
   if l == []:
      return []
   return reverse_list(l[1:]) + list(l[0])
   

def main():
   print((reverse_list(list(""))))
   
if __name__ == "__main__":
   main()