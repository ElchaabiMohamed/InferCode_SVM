def polynome(a,b,c):
    d=b*b-4*a*c
    x1=()
    x2=()
    if d>0:
      x1=-b-sqrt(d)/(2*a)
      x2=-b+sqrt(d)/(2*a)
    elif d==0:
      x1=-b/2*a
 