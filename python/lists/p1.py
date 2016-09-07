#!/usr/bin/python

n = int(raw_input().strip())
string = raw_input().strip()

num_arr = string.split(' ')
num_arr = [int(el) for el in num_arr]

print(hash(tuple(num_arr)))

