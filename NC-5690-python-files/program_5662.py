def ecart(liste):
    if liste==[]:
      return None
    elif len(liste)==1:
      return 0
    else:
      res=liste[0]
      max=0
      min=0
      for i in range(1,len(liste)):
        if res>liste[i]:
          max=liste[i]
      for i in range(1,len(liste)):
        if res<liste[i]:
          min=liste[i]
      ecart=max-min
      return ecart
          
      
      
      