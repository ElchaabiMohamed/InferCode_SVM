def moyenne(liste):
    if len(liste)==0:
      res=None
    else:
      res=0
      cpt=0
      moy=0
      for elem in liste:
        res=res+elem
        cpt=cpt+1
      moy=res/cpt
    return moy
  
  