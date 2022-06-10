#!usr/bin/env python3
import sys


def overlap(x1, y1, r1, x2, y2, r2):

    print((((x2 - x1)**2) + ((y2 - y1)**2) < ((r1 + r2)**2)))
