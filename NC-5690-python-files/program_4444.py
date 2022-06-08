def distribution(liste,n):
    res=[0]*(n+1)
    for i in range(len(liste)):
      for i in range(n+1):
        if liste[i]==i:
          res[i]=res[i]+1
    return res


  
  
