def nbVoyelles(mot):
    res=0
    for i in range (mot) :
      if liste[i] =='a,e,i,o,u,y' :
        res=res+1
    return res