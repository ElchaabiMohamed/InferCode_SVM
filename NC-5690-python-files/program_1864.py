def polynome(a,b,c):
  res="pas de solution"
  delta=b**2-4*a*c
  if delta>0:
    S1=(-b+delta**(1/2))/2*a
    S2=(-b-delta**(1/2))/2*a
  return res