def moyenne(liste):
  if len(liste)==0:
    res=None
  else:
    cpt=0
    num=0
    res=0
    for i in range(len(liste)):
      num=num+liste[i]
      cpt=cpt+1
    res=num/cpt
  return res