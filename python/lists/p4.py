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

def find_min_grade(students):
  min_grade = sys.maxint
  for person in students:
    if person[1] < min_grade:
      min_grade = person[1]

  return min_grade

def find_next_min_grade(students, min_grade):
  next_min_grade = sys.maxint
  for person in students:
    if person[1] < next_min_grade and person[1] > min_grade:
      next_min_grade = person[1]

  return next_min_grade

def find_students_with_next_min_grade(students, next_min_grade):
  result = []
  for person in students:
    if person[1] == next_min_grade:
      result.append(person[0])

  return result

#students = [[1, 'mike'], [2.2, 'john'], [2.2, 'merry']]

n = int(raw_input().strip())
students = []
s = []

for i in xrange(0, n*2):
  arg = raw_input().strip()
  
  if isint(arg):
    arg = int(arg)
  elif isfloat(arg):
    arg = float(arg) 

  s.append(arg)
  if i % 2:
    students.append(s)
    s = []

min_grade = find_min_grade(students)
next_min_grade = find_next_min_grade(students, min_grade)
result = find_students_with_next_min_grade(students, next_min_grade)

#print(students)
#print("Min grade: %f" % min_grade)
#print("Next min grade: %f" % next_min_grade)
#print(result)

result.sort()
for name in result:
  print(name)
