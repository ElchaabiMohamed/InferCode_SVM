def doubleLettre(mot):
  lettre2 = ' '
  res = False
  for lettre1 in mot :
    if lettre1 == lettre2 :
      res = True
    lettre2 = lettre1
  return res