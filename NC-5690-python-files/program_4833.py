def doubleLettre(mot):
  res=False 
  c1=''
  for c2 in mot:
    c1=c2
    if c1=='' and c2=='':
      res=True
  return res
      
    
	