def polynome(a,b,c):
  from math import sqrt
  res="pas de solution"
  delta=b**2-4*a*c
  if delta>0:
    res=(-b+print(sqrt(delta)))/2*a
  return res