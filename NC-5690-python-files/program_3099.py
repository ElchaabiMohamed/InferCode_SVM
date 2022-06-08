def sommeNbPairs(liste):
    res=0
    for i in range (len(liste)):
      if i%2==0 :
        res= res+liste[i]
    return res