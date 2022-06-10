#!/usr/bin/env python3

import sys

def swap_keys_values(d):
	return {p[0] : p[1] for p in list(d.items())}