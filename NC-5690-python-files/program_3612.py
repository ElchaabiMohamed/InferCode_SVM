def moyenne(liste):
  if len(liste)==0:
    return None
  else:
    moy = 0
    for i in liste:
    	moy+=i
    moy/=len(liste)
  return moy