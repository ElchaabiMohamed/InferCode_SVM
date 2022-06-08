def listeMatchs(liste):
    if len(liste)>0:
      res=[]
      for i in range(len(liste)-1):
        for j in range(i+1,len(liste)):
          res.append([(liste[i],liste[j])])
    return res
        