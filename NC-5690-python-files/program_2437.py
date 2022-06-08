def listeMatchs(liste):
  res=[]
  for i in range(len(liste)):
    for j in range(i,len(liste)):
      res.append((liste[i],liste[j]))
  return None