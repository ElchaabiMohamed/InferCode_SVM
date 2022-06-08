def prononcable(mot):
    res = True
    liste_voyelles = ["a","e","i","o","u","y"]
    nb_ = 0
    last = ""
    for lettre in range(mot):
        if lettre.lower() in liste_voyelles:
            if last == "syl":
        	    nb = 0
            last = "voy"
            nb += 1
        else:
            if last == "voy":
        	    nb = 0
            last = "syl"
            nb += 1

        if nb_ == 3:
            res = False
    return res
        
          
    