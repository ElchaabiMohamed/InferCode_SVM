def plusLongueSuite(liste):
    if liste==[]:
      res=0
    else:
      cpt=1
      cptMax=1
      prec=liste[0]
      for i in range(1,len(liste)):
        if prec==liste[i]:
          cpt+=1
          if cpt>cptMax:
            cptMax=cpt
        else:
          cpt=0
        prec=liste[i]
    return cptMax
      