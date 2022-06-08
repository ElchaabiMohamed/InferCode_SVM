def sommeNbPairs(liste):
    res=0
    for c in liste:
        if c%2==0:
          res=res+c
    return res