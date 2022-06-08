def listeMatchs(liste):
    if len(liste)>0:
      res=[]
      l=()
      for i in range(len(liste)-1):
        for j in range(i+1,len(liste)):
          l=(liste[i],liste[j])
          res+=[l]
      return res
    return []
  
        