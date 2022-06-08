def permutationListe(liste,permutation):
    res = [0]*len(liste)
    for i in range (len(liste)) :
      res.append(liste[permutation[i]])
    return res