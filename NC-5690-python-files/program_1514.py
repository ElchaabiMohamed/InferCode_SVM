def moyenne(liste):
  if len(liste)==0:
    res=None
  else:
    res=0
    x=0
    for i in range(len(liste)):
      res=res+i
      x=x+1
  moy=x%res
  return moy