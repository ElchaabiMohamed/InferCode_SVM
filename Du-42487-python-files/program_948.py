def reverse(a):
  rev = []
  i = 0
  for i in len(a):
    rev.append(a[len(a) - i - 1])
  return rev
