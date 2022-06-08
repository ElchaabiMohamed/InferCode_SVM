def ecart(liste):
    if liste==[]:
      res=None
    else:
      x=min(liste)
      y=max(liste)
      res=abs(x-y)
    return res