def polynome(a,b,c):
  delta = (b**2)-(4*a*c)
  if delta < 0 :
    res = ("pas de solution")
  elif delta == 0 :
    res = (-b)/(2*a)
  else :
    x1 = (-b + delta**(1/2))/2*a
    x2 = (-b - delta**(1/2))/2*a
    res = (x1 , x2)
  return res