def nbVoyelles(mot):
    cpt=0
    for lettre in mot:
      if lettre==["a", "e", "i", "o", "u", "y"]:
        cpt=cpt+1
    return cpt
  