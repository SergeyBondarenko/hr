#!/usr/bin/python

string = raw_input().strip()
alnum, alpha, digit, lower, upper = False, False, False, False, False

for char in string:
  if char.isalnum():
    alnum = True
  if char.isalpha():
    alpha = True
  if char.isdigit():
    digit = True
  if char.islower():
    lower = True
  if char.isupper():
    upper = True

print(alnum)
print(alpha)
print(digit)
print(lower)
print(upper)

