#!/usr/bin/python

name = []

for i in range(2):
    name.append(raw_input().strip())

print('Hello %s %s! You just delved into python.' % (name[0], name[1]))
