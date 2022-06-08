def polynome(a,b,c):
  res= 0
  delta= b**2-4*a*c
  if delta > 0:
    res= ((-b+delta**(1/2))/2*a, (-b-delta**(1/2))/2*a)
  elif delta==0:
    res= -b/2*a
  else:
    res= 'pas de solution'
  return res