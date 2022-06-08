from math import *
def polynome(a,b,c):
  D=(b*b)-4*a*c
  if D>0 :
    RacineD=sqrt(D)
    x1=(-b+RacineD)/(2*a)
    x2=(-b-RacineD)/(2*a)
    res=(x1,x2)
  elif D==0 :
    x0=-b/(2*a)
    res=x0
  else :
    res="pas de solution"
  
  return res