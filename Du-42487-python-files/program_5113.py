#!/usr/bin/env python

i = 1
f = "Fizz"
b = "Buzz"
while i < 101:
  if (i % 3 == 0) and (i % 5 == 0):
    print(f + b)
  elif i % 3 == 0:
    print(f)
  elif i % 5 == 0:
    print(b)
  else:
    print(i)
  i = i + 1
