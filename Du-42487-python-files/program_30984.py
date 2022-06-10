#!/usr/bin/env python3

def power(m, n):
    if m == 1:
        return 1
    return m ** power(m, n)