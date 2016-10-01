#!/usr/bin/python

task = {}
for i in xrange(2):
  arg = raw_input().strip()
  if i == 0:
    task.update({"str": arg})
  else:
    arg = arg.split(" ")
    task.update({"index": int(arg[0])})
    task.update({"letter": arg[1]})

#task = {'index': 1, 'letter': 'h', 'str': 'hello'}
string = task['str'][:task['index']] + task['letter'] + task['str'][task['index'] + 1:]
print(string)
