def semestreValide(ue1,ue2):
  if ue1 < 10 :
    res = False
  elif ue1 >= 10 and ue2 < 10 :
    if ((ue1 + ue2) /2) >= 10 :
      res = True
    else :
      res = False
  else :
  	res = True
   
      
  return res