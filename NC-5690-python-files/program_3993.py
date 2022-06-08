def polynome(a,b,c):
  delta=b**2-4*a*c
  if delta<0:
    res="pas de solution"
  if delta==0:
    sol1=str(b/2*a)
    res="la solution est "+sol1
  if delta>0:
    sol1=str((b*sqrt(delta))/2)
    sol2=str(b*(sqrt(delta)/2))
    res="les solutions sont "+sol1+" et "+sol2
  return None