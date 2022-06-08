def prononcable(mot):
  if mot=='':
    res=True
  else:
    res=True
    Voyelles=['a','e','i','o','u','y']
    ch=""
    for i in range(len(mot)):
      if mot[i] in Voyelles:
        ch=ch+"1"
      elif mot[i] not in Voyelles:
        ch=ch+"0"
    if "0000" in ch or "1111" in ch :
      res=False
  return res