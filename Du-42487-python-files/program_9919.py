#!usr/bin/env python3

def power(n, m):
    return 1 if not m else n * power(n, m - 1)
