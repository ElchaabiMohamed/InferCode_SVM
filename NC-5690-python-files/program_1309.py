def ecart(liste):
    if len(liste)==0:
      res=None
    else:
      res=liste[0]
      max=[]
      min=[]
      for i in range(1,len(liste)):
        if liste[i]<res:
          min=liste[i]
        if liste[i]>res:
          max=liste[i]
          res=max-min
    return res
      
      