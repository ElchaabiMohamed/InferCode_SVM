#!usr/bin/env python3


def maximum(l):
    return l[0] if len(l) == 1 else max(l[0], maximum(l[1:]))
