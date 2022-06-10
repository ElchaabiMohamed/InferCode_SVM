#!/usr/bin/env python3

def count_letters(word):
    if not word:
        return 0
    return 1 + word[:-1]
