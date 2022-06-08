def moyenne(liste):
  if len(liste)==0:
    moy=None
  else:
    moy=0
  for i in liste:
    moy=moy+i
  moy= moy/len(liste)
  return moy