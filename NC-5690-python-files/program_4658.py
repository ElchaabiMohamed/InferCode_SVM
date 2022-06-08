def nbVoyelles(mot):
    if mot=='':
      cpt=0
    else:
      cpt=0
      for c in mot:
        if c in 'aeiouy':
          cpt+=1
    return cpt