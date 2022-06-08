def polynome(a,b,c):
  import math
  delta=pow(b,2)-4*a*c
  if delta>0:
    res=((-b-math.sqrt(delta))/2*a,(-b+math.sqrt(delta))/2*a)
  if delta==0:
    res=-b/a
  else:
    res='pas de solution'
  return res