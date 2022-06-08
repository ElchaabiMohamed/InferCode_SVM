def nbOccurrencesLettre(lettre,mot):
    if lettre=='' or mot=='':
      res=0
    else:
      cpt=0
      for c in mot:
        if lettre==c:
          cpt=cpt+1
    return res