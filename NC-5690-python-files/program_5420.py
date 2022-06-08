def polynome(a,b,c):
    a=int(input())
    b=int(input())
    c=int(input())
    d=((b*b)-(4*a*c))
    print("delta=",d)
    if d<0:
      print("pas de solution")
    else:
      if d>0:
        x1=(-b + sqrt(d))/(2*a)
        x2=(-b - sqrt(d))/(2*a)
        print("les deux réponses sont",x1,"et",x2)
      else:
        print("la solution est",-b/(2*a))
 