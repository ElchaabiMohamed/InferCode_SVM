def phrasePalindrome(phrase):
    flagIn = 0
    flagOut = len(phrase)-1
    trouve = False
    while flagOut > flagIn and not trouve:
        if phrase[flagOut] == " ":
          flagOut -= 1
        if phrase[flagIn] == " ":
          flagIn += 1
        if phrase[flagIn] == phrase[flagOut]:
          flagIn += 1
          flagOut -= 1
        else:
          trouve = True
    if trouve == False:
      res = True
    else:
      res = False
    return res