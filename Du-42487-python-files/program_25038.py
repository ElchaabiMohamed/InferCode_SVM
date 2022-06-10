#!/usr/bin/env python

v = 0

i = 0
while i < 10:
  n = eval(input())
  if n < v:
    v = n
  i = i + 1

print(v)
