def semestreValide(ue1,ue2):
  if ue1 < 10 :
    if ue2 >= 10 :
    	res = True
    else :
    	res = False 
  else :
    if ue2 >= 10 :
    	res = True
    else :
    	res = False
      
  return res