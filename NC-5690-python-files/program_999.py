def distribution(liste,n):
    res=[0]*(n+1)
    for i in range(len(liste)):
      for i in range(n+1):
        if liste[i]==n:
          res[i]=res[n]+1
    return res


  
  
