def semestreValide(ue1,ue2):
  if ue1<10:
    res=False
  if ue1>=10 and ue2>=10 or ue1>=10 and ue2<10 and ue1+ue2>=20:
    res=True
  return res