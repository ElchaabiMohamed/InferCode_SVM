def motPalindrme(mot):
  res=False
  if mot=='':
    res=True
  else:
    mot2=''
    for i in mot:
      mot2=i+mot2
    if mot1==mot2:
      res=True
  return res
  