def reconstruireChainePartielle(s,n):
    res = ""
    for i in range (len(s),n) :
      res = res + [i]
    return res