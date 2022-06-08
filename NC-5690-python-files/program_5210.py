def polynome(a,b,c):
    res=0
    det=b**2-4*a*c
    if det>0:
      x1=-b-(racine(det))/2*a
      x2=-b+(racine(det))/2*a
      res=x1,x2
    elif det<0:
      res=0
    else:
      res=-b/2*a
    return res
      
 

 