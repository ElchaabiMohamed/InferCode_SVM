def semestreValide(ue1,ue2):
  moyenne=(ue1+ue2)/2
  if ue1>=10 and ue2>=10:
    return True
  elif ue1>ue2 and moyenne>=10:
    return True
  else:
    return False