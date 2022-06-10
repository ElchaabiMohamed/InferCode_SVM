#!usr/bin/env python3

def count_letters(s):
    return 0 if not s else count_letters(s[1:]) + 1
