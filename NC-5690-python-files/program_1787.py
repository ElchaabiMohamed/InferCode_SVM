def permutationListe(liste,permutation):
    res = [0]*len(liste)
    for i in range (len(liste)) :
      for elem in permutation :
        if elem == i :
          res[elem]=liste[i]
    return res