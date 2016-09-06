#!/usr/bin/python

digit = 2
numbers = []

for i in range(digit):
    numbers.append(int(raw_input().strip()))

print(numbers[0] + numbers[1])
print(numbers[0] - numbers[1])
print(numbers[0] * numbers[1])
