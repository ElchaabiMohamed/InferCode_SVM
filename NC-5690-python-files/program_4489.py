def qualifJO(sexe,record,nbvictoires,champion):
  if champion==True:
    res=True
  else:
    if M==sexe and record<12.0 and nbvictoires>=3:
      res=True
    elif F==sexe and record<15.0 and nbvictoires>=3:
      res=True
    else:
      res=False
  return res