def semestreValide(ue1,ue2):
  if ue1==10 and ue2==10:
    return True
  if ue1>ue2 or ue1<ue2:
    return True
  else:
    return False