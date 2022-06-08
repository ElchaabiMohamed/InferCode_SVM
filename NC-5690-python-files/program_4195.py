def qualifJO(sexe,record,nbvictoires,champion):
  if champion==True:
    res=True
  else:#False continuer la fonction 
    if sexe==M:
      if record<12:
        if nbvictoires>=3:
          res=True
    if sexe==F:
      if record<15:
        if nbvictoires>=3:
          res=True
    else:
      res=False
  return res