def moyenne(liste):
  if liste==():
    res=none
  else:
    x=0
    cpt=0
    for i in range(len(liste)):
      cpt=cpt+1
      x=x+liste[i]
    res=x/cpt
  return res