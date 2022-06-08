def motPalindrome(mot):
    flag = 0
    trouve = False
    if mot == "":
        res = True
    else:
        while flag <= len(mot) // 2 and not trouve:
            if mot[flag] == mot[-flag-1]:
                flag += 1
            else:
                trouve = True
                res = False
    if trouve == False:
        res = True
    return res