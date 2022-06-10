#!/usr/bin/env python

def reverse_list(l = []):
	if l.isempty():
		return '[]'
	for i in reversed(l):
		return list(i)

