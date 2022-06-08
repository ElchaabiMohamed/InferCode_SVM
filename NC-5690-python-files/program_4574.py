def permutationListe(liste,permutation):
  liste2=[0]*len(liste)
  for i in liste:
    liste[i]=permutation[i]
    liste2[i]=liste[i]
  return liste2
    
  
    
  