def reverse(a):
  rev = []
  i = 0
  while i < len(a):
    rev.append(a[len(a) - i - 1])
    i = i + 1
  return rev
