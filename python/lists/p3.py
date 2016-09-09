#!/usr/bin/python

import pdb
import sys

n = int(raw_input().strip())
arr = [int(el) for el in raw_input().strip().split(' ')]

maxi = max(arr)
next_maxi = 0 - sys.maxint
for i in arr:
    if i != maxi and i > next_maxi:
        next_maxi = i

print(next_maxi)

