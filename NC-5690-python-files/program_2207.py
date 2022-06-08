def moyenne(liste):
  if len (liste)==0:
    res=None
  else:
    res=1
    cpt=1
    for elem in range(len(liste)):
      res=res+elem
      cpt=cpt+1
      res=res%cpt
  return res 