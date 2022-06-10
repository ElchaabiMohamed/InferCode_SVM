#!/usr/bin/env python3

import sys

def swap_unique_keys_values(d):
	return {(b , a) for (a , b) in list(d.items()) if (list(d.values())).count(b) == 1}

