def qualifJO(sexe,record,nbvictoires,champion):
  res=False
  if sexe==M and champion:
    res=True
  elif record<12.0 and nbvictoires>=3:
    res=True
  if sexe==F and champion:
    res=True
  elif record<15 and nbvictoires>=3:
    res=True
  return res