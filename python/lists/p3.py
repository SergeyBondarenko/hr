#!/usr/bin/python

import pdb

#n = int(raw_input().strip())
#arr = raw_input().strip().split(' ')
#for i in xrange(len(arr)): arr[i] = int(arr[i])

#arr = [1, -1, -2, -1]
#arr = [-7, -7, -7, -6]
arr = [50, 100, 50]

maxi = max(arr)
next_maxi = 0

for i in arr:
    if i != maxi: 
        if i > next_maxi:
            next_maxi = i

print(next_maxi)

