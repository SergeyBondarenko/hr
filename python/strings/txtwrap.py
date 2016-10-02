#!/usr/bin/python

import textwrap

args = []
for i in xrange(2):
  a = raw_input().strip()
  if i == 1:
    a = int(a)
  args.append(a)

string = args[0]
num = args[1]

print(textwrap.fill(string, num))
