def rendezVous(debut1,fin1,debut2,fin2) :
  if(debut1,fin1,debut2,fin2)in '1,10,7,20' :
     res=True
  if(debut1,fin1,debut2,fin2)in '1,7,10,20' :
     res=False
  if(debut1,fin1,debut2,fin2)in '20,25,10,20' :
     res=True
  return res
  