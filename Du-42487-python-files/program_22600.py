#!/usr/bin/env python3
import sys

def maximum(l):
   if len(l) == 1:
      return l[0]
   if l[0] < l[-1]:
      return maximum(l[1:])
   else:
      return maximum(l[:-1])

def main():
   print((maximum([5, 6, -4, 3])))
   
if __name__ == "__main__":
   main()