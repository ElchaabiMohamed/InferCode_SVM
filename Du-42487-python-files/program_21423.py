#!/usr/bin/env python

def double(n):
  return n * 2

n = input()

if n.isdigit():
   n = int(n)

print(double(n))
