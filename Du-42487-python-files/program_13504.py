#!/usr/bin/env python

import sys

new = ""
i = 0
while i < len(sys.argv):
   s = len(sys.argv)-i-1
   new = new + str(s)
   i = i+1
