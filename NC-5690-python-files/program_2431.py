def nbVoyelles(mot):
    cpt=0
    for lettre in mot: 
      if lettre in 'aeiouy':
        cpt=cpt+1
    return cpt