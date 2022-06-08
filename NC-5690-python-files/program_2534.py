def polynome(a,b,c):
    delta=(b**2)-(4*a*c)
    if delta<0:
      return("pas de solution")
    x=((-b-(sqrt(delta)))/(2*a))
    y=((-b+(sqrt(delta)))/(2*a))
    if delta>0:
      return(x,y)
    if delta==0:
      return(x)
 

 