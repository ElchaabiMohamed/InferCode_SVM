def polynome(a,b,c):
    det=b**2-4*a*c
    if det>0:
      sol1=-b-det**0,5/2*a
      sol2=-b+det**0,5/2*a
      res=(sol1,sol2)
    elif det==0:
      res=-b/2*a
    else:
      res="pas de solution"
    
      
 

 