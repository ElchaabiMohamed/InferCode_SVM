def prononcable(mot):
    listvoy = ["a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U", "Y", " ", "è", "é", "à"]
    cons = 0
    for lettre in mot:
        if lettre not in listvoy:
            cons += 1
        elif cons >= 4:
            return False
        else:
            cons = 0
    return True