def nbVoyelles(mot):
    cpt=0
    for c in mot:
      if c=="a,e,i,o,u,y":
        cpt=cpt+1
    return cpt
  