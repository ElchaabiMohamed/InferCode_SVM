import sys


def swap_unique_keys_values(d):
  a = {}
  b = {}
  c = sorted(list(d.items()), reverse = True)
  for k,v in c:
    if v not in b:
      b[v] = k
    else:
      b[v] = "A"
  e = sorted(list(a.items()), reverse = True)
  for k,v in e:
    if v != "A":
      b = v
  return b