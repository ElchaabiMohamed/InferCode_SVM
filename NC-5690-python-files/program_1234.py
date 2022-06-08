def doubleLettre(mot):
  res=False
  bib=''
  for l in mot:
    if l==bib:
      res= True
    bib=l
  return res
      
    
	