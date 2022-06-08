def moyenne(liste):
  res=0
  cpt=0
  if len(liste)==0:
    res=0
  else:
     for i in liste:
       res=res+i
       cpt=cpt+1
  res=res%cpt
  return res