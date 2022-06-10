def minimum(a):
  if len(a) == 1:
    return a[0]
  else:
    return min(a[0],minimum(a[1:]))