#!/usr/bin/python
import pdb

def is_leap(year):
    leap = False
    if year % 100 == 0 and year % 400 != 0:
        leap = False
    elif year % 4 == 0:
        leap = True

    return leap


year = int(raw_input().strip())
print(is_leap(year))
