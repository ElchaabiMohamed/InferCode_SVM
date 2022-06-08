from math import *

def polynome(a,b,c):
  d=b**2-4*a*c
  if d <0:
    return "pas de solution"
  elif d==0:
    x1==-b/2*a and x2==-b/2*a
    return x1 and x2
  elif d>0:
    s1=(-b-(sqrt(d)))/2*a
    s2=(-b+(sqrt(d)))/2*a
    return s1 and s2

    polynome(1,-1,0)
    polynome(2,-4,2)
    polynome(3,-2,10)