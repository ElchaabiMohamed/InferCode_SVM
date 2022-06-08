def semestreValide(ue1,ue2):
  if ue1>=10 and ue2>=10:
    res=True
  elif ue1>=10 and (ue1+ue2)/2>=10:
    res=True
  else:
    res=False
  return res