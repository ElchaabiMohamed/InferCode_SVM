def moyenne(liste):
  res=0
  cpt=0
  if len(liste)==0:
    moy=None
  else:
     for i in liste:
       res=res+i
       cpt=cpt+1
  moy=res*cpt
  return moy