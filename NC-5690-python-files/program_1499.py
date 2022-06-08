def compareDates(jour1,mois1,annee1,jour2,mois2,annee2):
    if annee1<annee and mois1<mois2 and jour1<jour2: 
      res=-1
    if annee1==annee2 and  mois1==mois2 and jour1==jour2: 
       res=0
    else : 
      res=1