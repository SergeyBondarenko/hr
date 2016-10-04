#!/usr/bin/python

# 97, ... 122
size = 3
for i in xrange(0, size, 1):
    print chr((97+(size-1))-i).center(size, '-')

