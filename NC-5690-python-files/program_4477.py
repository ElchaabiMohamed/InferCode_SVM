def compareDates(jour1,mois1,annee1,jour2,mois2,annee2):
  
  res=0
  for elem in jour1,mois1,annee1,jour2,mois2,annee2:
    
    if ('jour1,mois1,annee1')<('jour2,mois2,annee2'):
       res=res-1
      
    elif ('jour1,mois1,annee1')==('jour2,mois2,annee2'):
       res=res
    
    elif ('jour1,mois1,annee1')<('jour2,mois2,annee2'):
       res=res+1
      
  return res