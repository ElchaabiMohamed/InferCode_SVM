def compareDates(jour1,mois1,annee1,jour2,mois2,annee2):
  
  res=0
  
  for elem in jour1,mois1,annee1,jour2,mois2,annee2:
    
    if ('mois1' and 'annee1')<('mois2 and ''annee2'):
       res=res-1
      
    if ('mois1' and 'annee1')==('mois2'and'annee2'):
       res=res
    
    if ('mois'and 'annee1')<('mois2'and'annee2'):
       res=res+1
      
  return res