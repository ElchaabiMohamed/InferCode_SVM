#!usr/bin/env python3

def minimum(l):
    return l[0] if len(l) == 1 else min(l[0], minimum(l[1:]))
