def prononcable(mot):
    if len(mot)==0:
      res=True
    else:
      res=False
      for i in range(len(mot)):
        if mot[i] in 'aeiouy' and mot[i]!=mot[i+3]:
          res=True
        if mot[i] in 'bcdfghjklmnpqrstvwxz' and mot[i]!=mot[i+3]:
          res=True
    return res
      