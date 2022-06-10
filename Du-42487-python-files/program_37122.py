#!usr/bin/env python3

def factorial(n):
    return n if n < 2 else n * factorial(n - 1)
