def nbVoyelles(mot):
    res=0
    for i in range (mot) :
      if i =='a,e,i,o,u,y' :
        res=res+1
    return res