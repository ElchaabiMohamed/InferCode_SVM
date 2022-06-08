def prononcable(mot):
    res = True
    liste_voyelles = ["a","e","i","o","u","y"]
    nb_ = 0
    last = ""
    for lettre in mot:
        if lettre.lower() in liste_voyelles:
            if last == "syl":
        	    nb_ = 0
            last = "voy"
            nb_ += 1
        else:
            if last == "voy":
        	    nb_ = 0
            last = "syl"
            nb_ += 1
        
        if nb_ > 3:
            res = False
    return res