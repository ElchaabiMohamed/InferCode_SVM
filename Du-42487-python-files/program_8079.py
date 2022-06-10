#!/usr/bin/env python
count = 0
i = 0
while i < 10:
    print(count)
    if count == 0:
        count = 1
    elif count == 1:
        count = 0
    i = i + 1
