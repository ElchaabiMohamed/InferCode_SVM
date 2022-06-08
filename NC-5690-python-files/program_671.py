def nbVoyelles(mot):
    res=0
    for i in range (len(mot)) :
      if mot[i] =='a,e,i,o,u,y' :
        res=res+1
    return res