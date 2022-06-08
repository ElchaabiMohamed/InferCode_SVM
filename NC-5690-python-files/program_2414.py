def nbVoyelles(mot):
    cpt=0
    for lettre in range(0,len(mot)):
      if lettre=="a":
        cpt=cpt+1
      if lettre=="e":
        cpt=cpt+1
      if lettre=="i":
        cpt=cpt=1
      if lettre=="o":
        cpt=cpt+1
      if lettre=="u":
        cpt=cpt+1
      if lettre=="y":
        cpt=cpt+1
    return cpt
  