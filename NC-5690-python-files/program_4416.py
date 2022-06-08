def compareDates(jour1,mois1,annee1,jour2,mois2,annee2):
  a=jour1-jour2
  b=mois1-mois2
  c=annee1-annee2
  if c!=0 :
    if c<0 :
      res=-1
    else :
      res=1
  elif b!=0 :
    if b<0 :
      res=-1
    else :
      res=1
  elif a!=0 :
    if a<0 :
      res=-1
    else :
      res=1
  else :
    res=0
    
  
  return res