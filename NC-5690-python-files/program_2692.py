def suiteGeo(liste):
  i=0
  j=0
  ok=True
  raison=None
  if len(liste)>1:
    while i<len(liste) and liste[0]!=0 and raison==None:
      raison=liste[i+1]/liste[i]
      i+=1
    while j<len(liste)-1 and ok:
      if liste[i+1]!=liste[i]*raison:
        ok=False
      i+=1
  return ok