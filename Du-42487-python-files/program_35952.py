#!usr/bin/env python3

def sumup(n): 
    return n if n < 2 else n + sumup(n - 1)
