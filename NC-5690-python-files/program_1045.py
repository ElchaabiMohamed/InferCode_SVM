def moyenne(liste):
    if liste==[]:
      res=None
    else:
      x=0
      cpt=0
      for i in range(len(liste)): 
        x=x+i
        cpt=cpt+1
       	res=x/cpt
      return res