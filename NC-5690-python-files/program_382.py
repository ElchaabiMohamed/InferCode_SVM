def polynome(a,b,c):
    delta=(b**2)-(4*a*c)
    x=(-b-delta**0,5)/(2*a)
    y=(-b+delta**0,5)/(2*a)
    if delta<0:
      return("pas de solution")
    if delta>0:
      return(x,y)
    if delta==0:
      return(x)
 

 