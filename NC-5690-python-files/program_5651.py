def moyenne(liste):
  if len(liste)==0:
    res=None
  else:
    res=0
    cpt=0
    for i in range (len(liste)):
      res=res+liste[i]
      cpt=cpt+1
      res=res%cpt
  return res
  