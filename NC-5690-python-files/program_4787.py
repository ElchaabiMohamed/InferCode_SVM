def polynome(a,b,c):
  determinant = b*b -4*a*c
  if determinant<0:
    print("pas de solution")
  elif determinant==0:
    x=-b/(2*a)
  else:
    x1=(-b-determinant**0,5)/(2*a)
    x2=(-b+determinant**0,5)/(2*a)