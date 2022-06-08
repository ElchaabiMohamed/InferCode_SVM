def permutationListe(liste,permutation):
    res = [0]*len(liste)
    for i in range (len(liste)) :
      for y in range (len(permutation)) :
        if permutation[y] == i :
          res[i] = liste[y]
    return res