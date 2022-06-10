#!/usr/bin/env python3

def count_letter(s):
	if len(s) == 0:
		return 0

	return 1 + count_letter(s[1:])
