def nbOccurrencesLettre(lettre_to_find,mot):
    res = 0
    if len(mot) > 0:
        for lettre in mot:
            if lettre == lettre_to_find:
                res += 1
    return res
