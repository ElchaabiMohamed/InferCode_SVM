def qualifJO(sexe,record,nbvictoires,champion):
  if champion==True:
    res=True
  elif champion==False:
    if sexe==M and record<12.0 and nbvictoires>=3:
      res=True
    elif sexe==F and record<15.0 and nbvictoires>=3:
      res=True
    else:
      res=False
  return res