#!/usr/bin/env python

import sys

print("stdin:", " ".join(sys.stdin.read().split()))
print("argv:", " ".join(sys.argv[1:]))
