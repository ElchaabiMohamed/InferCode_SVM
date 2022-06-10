#!/usr/bin/env python


x = int(raw_input())

if (x%3) == (x%5) ==0:
	print "fizz-buzz"
elif  (x%3)==0:
	print "fizz"
else (x%5)==0:
	print "buzz"

