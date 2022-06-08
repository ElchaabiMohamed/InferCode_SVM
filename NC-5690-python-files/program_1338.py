def ecart(liste):
    if len(liste)==0:
      res=None
    else:
      res=liste[0]
      maxi=[]
      mini=[]
      for i in range(1,len(liste)):
        if liste[i]<res:
          mini=liste[i]
        if liste[i]>res:
          maxi=liste[i]
          res=maxi-mini
    return res
      
      