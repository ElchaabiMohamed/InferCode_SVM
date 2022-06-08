def qualifJO(sexe,record,nbvictoires,champion):
  res = True
  if sexe == 'M':
    if record < 12 or nbvictoires < 3 :
      res = False
      if champion == True :
        res = True
  else :
    if record < 15 or nbvictoires < 3 :
      res = False
      if champion == True :
        res = True
  return res