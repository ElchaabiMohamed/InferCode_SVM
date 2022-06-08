def listeMatchs(liste):
  lmatchs=[]
  i=0
  j=i+1
  while i<len(liste)-1:
    lmatchs+=[(liste[i],liste[i+1])]
    j+=1
    if j>=len(listes):
      i+=1
      j=i+1
  return lmatchs