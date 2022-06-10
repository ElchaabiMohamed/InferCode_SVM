#!/usr/bin/env python
i = 0
while i < 10:
    x = i % 5
    i = i + 1
    if x % 2 == 0:
        print(x)
