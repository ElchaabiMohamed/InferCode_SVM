def sommeNbPairs(liste):
    if liste==[]:
      res=0
    else:
      res=0
      for i in liste:
        if i%2==0:
          res=res+i
    return res