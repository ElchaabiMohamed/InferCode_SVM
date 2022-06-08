def listeMatchs(liste):
  res=[]
  for i in range(len(liste)):
    for j in range(i+1,len(liste)):
      res.append((liste[i],liste[j]))
  return res