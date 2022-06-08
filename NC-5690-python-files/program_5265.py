def sommeNbPairs(liste):
    if len(liste)==0:
      res=0
    else:
      res=0
      for i in range(0,liste):
        if liste[i]%2==0:
          res=res+liste[i]
    return res