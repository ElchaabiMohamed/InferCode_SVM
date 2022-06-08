def qualifJO(sexe,record,nbvictoires,champion):
  if champion:
    return True
  elif nbVictoires <3:
    return False
  else:
    if sexe=='M':
      if record<12:
        return True
    else:
      if record<15:
        return True
    return False