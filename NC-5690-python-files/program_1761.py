def polynome(a,b,c):
  import math
  delta=b**2-4*a*c
  if delta>0:
    x1=(-b+(math.sqrt(delta)))/2*a
    x2=(-b-(math.sqrt(delta)))/2*a
    res=(x1,x2)
  elif delta==0:
    x=(-b)/(2*a)
    res=x
  else:
    res='pas de solution'
  return res