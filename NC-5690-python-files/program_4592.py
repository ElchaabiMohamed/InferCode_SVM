def prononcable(mot):
    if len(mot)==0:
      res=True
    else:
      res=False
      for i in range(len(mot)):
        if mot[i] in 'aeiouy' and mot[i+3] not in 'aeiouy':
          res=True
    return res

                                     