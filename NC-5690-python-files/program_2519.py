def polynome(a,b,c):
    res=0
    det=b**2-4*a*c
    if det>0:
      x1=-b-det**0,5/2*a
      x2=-b+det**0,5/2*a
      res=x1,x2
    elif det==0:
      res=-b/2*a
    else:
      res="pas de solution"
    return res
      
 

 