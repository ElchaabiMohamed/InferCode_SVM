def nbVoyelles(mot):
    if len(mot)==0:
      cpt=0
    else:
      cpt=0
      for c in mot:
        if c in 'aeiouy':
          cpt=cpt+1
    return cpt