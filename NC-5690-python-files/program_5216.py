def moyenne(liste):
  if len(liste)==0:
    return None
  res=0
  cpt=0
  for i in range (len(liste)):
    res=res+liste[i]
    cpt=cpt+1
  if cpt==0:
    return None
  else:
    res=res/cpt
  return res