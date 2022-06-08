def permutationListe(liste,permutation):
    res = []
    for i in range (len(liste)) :
      res.append(liste[permutation[i]])
    return res