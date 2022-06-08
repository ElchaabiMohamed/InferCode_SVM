def polynome(a,b,c):
  res="pas de solution"
  delta=b**2-4*a*c
  if delta>0:
    res=(-b+sqrt(delta))/2*a
  return res