def qualifJO(sexe,record,nbvictoires,champion):
  res=False
  if sexe=='M':
    if record<12 and nbvictoires>=3 or champion==True:
      res=True  
  else:
    if record<15 and nbvictoires>=3 or champion==True:
      res=True
  return res