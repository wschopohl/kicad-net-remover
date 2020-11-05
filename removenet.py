#!/usr/bin/env python3

import sys
import re

def create_net_start_re(netname):
  net_start_re = r'\(net\s+(\(code\s+[0-9]+\)\s+)?\(name\s+"{netname_re}"|{netname_re}\)'.format(netname_re=re.escape(netname))
  return re.compile(net_start_re)

net_start_re = create_net_start_re(sys.argv[3])
node_re = re.compile(r'^\s*\(node\s+\(ref \w+\)\s+\(pin\s+\d+\)\s*\)(\)?)(.*)$')

def test_re():
  net_start_re = create_net_start_re('Net-(Q2-Pad2)')
  assert net_start_re.search('    (net (code 34) (name "Net-(Q2-Pad2)")')
  net_start_re = create_net_start_re('/LG1')
  assert net_start_re.search('(net (code 32) (name /LG1)')

  m = node_re.match("      (node (ref Q3) (pin 2))")
  assert m
  assert m[1] == ""
  assert m[2] == ""
  m = node_re.match("      (node (ref R22) (pin 2)))")
  assert m
  assert m[1] == ")"
  assert m[2] == ""
  m = node_re.match("      (node (ref J10) (pin 37)))))")
  assert m
  assert m[1] == ")"
  assert m[2] == "))"

test_re()

with open(sys.argv[1]) as search:
  with open(sys.argv[2], 'w') as output:
    net_found = False
    for line in search:
      tmpline = line.strip()
      if net_found:
        m = node_re.match(tmpline)
        if m:
          # Output any suffix after the match, if any.
          # This is to handle the case of matching the last net in file.
          # which require us to output closing ))), which are likely on the
          # same line.
          closing = m.group(1)
          if closing:
            net_found = False
          suffix = m.group(2)
          if suffix:
            output.write(suffix + "\n")
          continue
      net_found = False
      if net_start_re.search(tmpline):
        net_found = True
        continue
      output.write(line)
