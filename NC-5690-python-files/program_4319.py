def polynome(a,b,c):
    res=0
    det=b**2-4*a*c
    if det>0:
      res=-b-(racine(det))/2*a
      res=-b+(racine(det))/2*a
    elif det<0:
      res=0
    else:
      res=-b/2*a
    return res
      
 

 