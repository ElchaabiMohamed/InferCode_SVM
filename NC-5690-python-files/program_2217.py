def polynome(a,b,c):
  delta=b-4*a*c
  if delta>0:
    res=(-b-sqrt(delta)/2*a,-b+sqrt(delta)/2*a)
  if delta==0:
    res=-b/a
  else:
    res='pas de solution'
  return res