def doubleLettre(mot):
  lettre2 = ' '
  cpt = 0
  res = False
  for lettre1 in mot :
    if lettre1 != lettre2 :
      cpt =  0
    else : 
      cpt = cpt + 1
      if cpt >= 2 :
        res = True
  	
  return res