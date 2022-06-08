def nbVoyelles(mot):
    res = 0
    liste_voyelles = ["a","e","i","o","u","y"]
    for lettre in mot:
        if lettre.lower() in liste_voyelles:
        	res += 1
    return res
