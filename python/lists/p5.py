#!/usr/bin/python

import sys

def isfloat(x):
  try:
    n = float(x)
  except ValueError:
    return False
  else:
    return True

def isint(x):
  try:
    n = int(x)
  except ValueError:
    return False
  else:
    return True

n = int(raw_input().strip())
students = {}

for i in xrange(0, n):
  arg = raw_input().strip().split(' ')
  name = arg[0]
  math = int(arg[1]) if isint(arg[1]) else float(arg[1])
  physics = int(arg[2]) if isint(arg[2]) else float(arg[2])
  chemistry = int(arg[3]) if isint(arg[3]) else float(arg[3])
  students.update({name: [math, physics, chemistry]})

name = raw_input().strip()

#students = {'arjun': [70, 98, 63], 'christina': [67, 68, 69], 'malika': [52, 56, 60]} 
#name = 'malika'
average = sum(students[name])/float(len(students[name]))

print("{0:.2f}".format(average))
