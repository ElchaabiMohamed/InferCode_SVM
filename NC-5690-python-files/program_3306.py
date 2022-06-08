def moyenne(liste):
  if len(liste)==0:
    res=None
  else:
    res=0
    cpt=0
    for i in range(len(liste)):
      cpt=cpt+1
      res=res+liste[i]
    res=res/cpt
  return res