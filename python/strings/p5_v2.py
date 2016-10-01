#!/usr/bin/python

task = {}
for i in xrange(2):
  arg = raw_input().strip()
  if i == 0:
    task.update({"str": arg})
  else:
    task.update({"substr": arg})

occur = 0
match = len(task["substr"])
for i in xrange(len(task['str'])):
  if i+match < len(task['str']) + 1:
    if task['str'][i:i+match] == task['substr']:
      occur += 1

print(occur)
