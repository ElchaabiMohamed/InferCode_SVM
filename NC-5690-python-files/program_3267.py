def rendezVous(debut1,fin1,debut2,fin2):
  if debut1 < debut2:
    if debut1 <= debut2 and debut2 <= fin1:
      res= True
    else:
      res= False
      
  else:
    if debut2 <= debut1 and debut1 <= fin2:
      res= True
    else:
      res= False
      
  return res
      


assert rendezVous(1, 10, 7, 20)== True
assert rendezVous(1, 7, 10,20)== False