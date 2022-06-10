#!/usr/bin/env python3

def count_letters(word):
    if not word:
        return 0
    return 1 + count_letters(word[:-1])
