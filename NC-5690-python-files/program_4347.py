from math import sqrt 

def polynome(a,b,c):
  d=b**2-(4*a*c)
  if d<0:
    return 'pas de solution'
  elif d==0:
    solution=-b/(2*a)
    return solution
  else:
    if d>0:
      solution1=[-b-(sqrt(d))]/2*a
      solution2=[-b+(sqrt(d))]/2*a
      return solution1 and solution2