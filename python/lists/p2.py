#!/usr/bin/python

from itertools import product

input_arr = []
[input_arr.append(int(raw_input().strip())) for i in range(4)]

X = input_arr[0]
Y = input_arr[1]
Z = input_arr[2]
N = input_arr[3]
#X, Y, Z, N = 1, 1, 1, 2

#result = []
#for x in range(X+1):
#    for y in range(Y+1):
#        for z in range(Z+1):
#            if x + y + z != N:
#                result.append([x, y, z])

result = [list([x,y,z]) for x in range(X+1) for y in range(Y+1) for z in range(Z+1) if x+y+z != N]
#result = [list(i) for i in product(range(X+1), range(Y+1), range(Z+1)) if sum(i) != N]

print(result)
