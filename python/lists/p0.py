#!/usr/bin/python

n = int(raw_input().strip())
commands = []
result = []

for i in range(n):
    commands.append(raw_input().strip())

for cmd in commands:

    args = cmd.split(' ')
    if len(args) == 3:
        index = int(args[1])
        value = int(args[2])
    elif len(args) == 2:
        value = int(args[1])

    if 'insert' in cmd:
        result.insert(index, value) 
    elif 'print' in cmd:
        print(result)
    elif 'remove' in cmd:
        result.remove(value)
    elif 'append' in cmd:
        result.append(value)
    elif 'sort' in cmd:
        result.sort()
    elif 'pop' in cmd:
        result.pop()
    elif 'reverse' in cmd:
        result.reverse()

