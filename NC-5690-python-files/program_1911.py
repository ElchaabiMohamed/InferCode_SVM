def polynome(a,b,c):
    delta=(b**2)-(4*a*c)
    
    if delta<0:
      return("pas de solution")
    elif delta>0:
      x=(-b-delta**0,5)/(2*a)
      y=(-b+delta**0,5)/(2*a)
      return(x,y)
    if delta==0:
      return(-b/a)
 

 