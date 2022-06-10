#!/usr/bin/env python3
import sys

def swap_unique_keys_values(d):
   new_d = {}
   for k, v in list(d.items()):
      if list(d.values()).count(v) == 1:
         new_d[v] = k
   return new_d

def main():
   pass
   
if __name__ == "__main__":
   main()