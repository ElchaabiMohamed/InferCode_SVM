def ecart(liste):
    if liste==[]:
      return None
    elif len(liste)==1:
      return 0
    else:
      res=liste[0]
      for i in range(1,len(liste)):
        max=0
        if res>liste[i]:
          max=liste[i]
      for i in range(1,len(liste)):
        min=0
        if res<liste[i]:
          min=liste[i]
      ecart=max-min
      return ecart
          
      
      
      