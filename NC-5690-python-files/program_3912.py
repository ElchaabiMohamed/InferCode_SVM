def semestreValide(ue1,ue2):
    if ue1>=10:
      if ue2<10:
        if (ue1+ue2)/2>=10:
          res=True
        else:
          res=False
      else:
        res=True
    else:
      res=False
    return res