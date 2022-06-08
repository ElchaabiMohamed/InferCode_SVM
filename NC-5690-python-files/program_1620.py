def ecart(liste):
    if liste==[]:
      res=None
    else:
      min=min(liste)
      max=max(liste)
      res=abs(max-min)
    return res