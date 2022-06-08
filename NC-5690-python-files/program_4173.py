def qualifJO(sexe,record,nbvictoires,champion):
  if champion==True:
    res=True
  elif sexe=='M' and record<12 and nbvictoires>3:
    res=True
  else:
    if sexe=='F' and record<15 and nbvictoires>3:
          res=True
    else:
      res=False
    return res