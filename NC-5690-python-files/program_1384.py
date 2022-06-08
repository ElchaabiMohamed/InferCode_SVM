def permutationListe(liste,permutation):
    res = []
    for i in range (len(liste)) :
      for elem in permutation :
        if elem == i :
          res.append(liste[elem])
    return res