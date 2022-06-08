from math import *

def polynome(a,b,c):
  d=b**2-4*a*c
  if d <0:
    return "pas de solution"
  elif d==0:
    x1==-b/2*a and x2==-b/2*a
    return x1 and x2
  elif d>0:
    x3==(-b-(sqrt(d)))/2*a
    x4==(-b+(sqrt(d)))/2*a
    return x3 and x4

    polynome(1,-1,0)
    polynome(2,-4,2)
    polynome(3,-2,10)