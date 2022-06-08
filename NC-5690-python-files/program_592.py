def plusLongueSuite(liste):
    if len(liste)==0:
      cptmax=0
    else:
      cpt=0
      cptmax=0
      for i in range(len(liste)):
        if liste[i]==liste[i+1]:
          cpt+=1
        else:
          if cpt>cptmax:
            cptmax=cpt
    return cptmax
        