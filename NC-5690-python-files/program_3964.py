def moyenne(liste):
    res=0
    y=0
    x=0
    for elem in liste : 
      y=y+1
      x=x+elem
      res=x/y
      if len(liste)==0:
         res=None
    return res