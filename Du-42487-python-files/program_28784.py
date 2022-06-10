def maximum(n):
  if len(n)==1:
    return n[0]
  maxr = maxi(n[1:])
  return n[0] if n[0] > maxr else minr
