def plusLongueSuite(liste):
    if len(liste)==0:
      cptMax=0
    else:
      elemPrec=None
      cpt=0
      cptMax=0
      for elem in liste:
        if elem==elemPrec:
          cpt+=1
        else:
          if cpt>cptMax:
            cptmax=cpt
          cpt=1
        elemPrec=elem
      if cpt>cptMax:
        cptMax=cpt
    return cptMax
        