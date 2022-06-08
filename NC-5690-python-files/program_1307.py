def motPalindrome(mot):
  res=False
  if mot=='':
    res=True
  else:
    mot2=''
    for i in mot:
      mot2=i+mot2
    if mot==mot2:
      res=True
  return res
  