#!/usr/bin/env python

import sys

def unique_key_values(d):
   unique_d = {}
   for k in d:
      if is_unique(d[k],d):
         unique_d[k] = d[k]
   return unique_d

def swap_unique_keys_values(d):
   d = unique_key_values(d)
   newd = {}
   for k in d:
      newd[d[k]] = k
   return newd

def is_unique(v,d):
   count = 0
   for key in d:
      if d[key] == v:
         count += 1
   return count == 1

def main():
   pass
      
   

if __name__ == "__main__":
   main()
