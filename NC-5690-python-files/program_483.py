def qualifJO(sexe,record,nbvictoires,champion):
    if sexe=='M':
      if (record<12.0 and nbvictoires>=3) or champion==True:
          res=True
      else:
          res=False
    elif sexe=='F':
      if (record<15.0 and nbvictoires>=3) or champion==True:
        res=True
      else:
        res=False
    else:
      res=False
    return res