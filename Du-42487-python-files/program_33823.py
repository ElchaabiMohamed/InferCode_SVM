#!/usr/bin/env python3

def count_letters(word):
    if word == "":
        return 0
    return 1 + count_letters(word[1:])