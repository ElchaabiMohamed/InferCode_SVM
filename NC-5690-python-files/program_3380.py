def doubleLettre(mot):
  lettre2 = ' '
  cpt = 0
  res = False
  for lettre1 in mot :
    if lettre1 == lettre2 :
      lettre2 = lettre1
      cpt =  cpt + 1
    else :
      cpt = 0
  if cpt > 2 :
    res = True
  return res