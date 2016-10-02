#!/usr/bin/python

num = int(raw_input().strip())

bin_pad = str(len(bin(num)[2:]))

for i in xrange(1, num + 1):
  _oct = int(oct(i)) 
  _hex = hex(i)[2:].upper()
  _bin = bin(i)[2:]

  format_str = '{0:>'+bin_pad+'} {1:>'+bin_pad+'} {2:>'+bin_pad+'} {3:>'+bin_pad+'}'
  print format_str.format(i, _oct, _hex, _bin)
