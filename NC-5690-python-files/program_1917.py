def polynome(a,b,c):
    import math
    delta=(b**2)-(4*a*c)
    if delta>0:
      x1=(-b-math.sqrt(delta))/(2*a)
      x2=(-b+math.sqrt(delta))/(2*a)
      print(x1,x2)
    elif delta==0:
      x0=-b/(2*a)
      print(x0)
    else:
      print('pas de solution')