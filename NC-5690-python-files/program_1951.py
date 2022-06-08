def qualifJO(sexe,record,nbvictoires,champion):
    if sexe=='M':
      if record<12.0 and nbvictoires>=3:
          res=True
      else:
        if champion==True:
          res=True
        else:
          res=False
    else:
      if record<15.0 and nbvictoires>=3:
        res=True
      else:
        if champion==True:
          res=True
        else:
          res=False
    return res