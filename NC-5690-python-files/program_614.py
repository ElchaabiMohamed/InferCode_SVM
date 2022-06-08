def phrasePalindrome(phrase):
    phrase = phrase.replace(" ","")
    res = False
    if(phrase == phrase[::-1]):
        res = True
    return res