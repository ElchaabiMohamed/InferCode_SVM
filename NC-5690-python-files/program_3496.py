def moyenne(liste):
  if len(liste)==0:
    res=None
  else:
    x=0
    cpt=0
    for i in range(len(liste)):
      cpt=cpt+1
      x=x+liste[i]
    res=x/cpt
  return res