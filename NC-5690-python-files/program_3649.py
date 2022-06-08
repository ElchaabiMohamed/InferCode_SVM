def polynome(a,b,c):
  delta=b^2-4*a*c
  if delta>0:
    x=(-b-(sqrt(delta))/2*a,-b+(sqrt(delta))/2*a)
  elif delta==0:
    x=-b/2*a
  else:
    x='pas de solution'
  return res