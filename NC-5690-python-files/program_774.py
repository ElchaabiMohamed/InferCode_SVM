def semestreValide(ue1,ue2):
    res=False
    if ue1>=10 and ue2>=10:
      res=True
    else:
      res=False
    if ue1>=10 and ue2<10:
      res=True
    else:
      res=False
    return res