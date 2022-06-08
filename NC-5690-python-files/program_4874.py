def semestreValide(ue1,ue2):
    res=False
    if ue1>=10.0 and ue2>=10.0:
      res=True
    else:
      res=False
    if ue1>=10.0 and ue2<10.0:
      res=True
    else:
      res=False
    return res