def listeMatchs(liste):
  lmatchs=[]
  i=0
  j=i+1
  while i<len(liste)-1:
    lmatchs+=[(liste[i],liste[j])]
    j+=1
    if j>=len(liste):
      i+=1
      j=i+1
  return lmatchs