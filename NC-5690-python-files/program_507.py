def moyenne(liste):
  somme=0
  cpt=0
  for elem in liste : 
    somme=somme+elem
    cpt=cpt+1
  res=somme/cpt
  return res