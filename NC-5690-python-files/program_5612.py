def prononcable(mot):
  if mot=='':
    res=True
  else:
    res=True
    Voyelles=['a','e','i','o','u','y']
    chiffres=[]
    for i in range(len(mot)):
      if mot[i]==Voyelles:
        chiffres.append(1)
      elif mot[i]!=Voyelles:
        chiffres.append(0)
    if [0,0,0,0]in chiffres or [1,1,1,1] in chiffres :
      res=False
  return res