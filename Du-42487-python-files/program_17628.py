def count_letters(word): 
   if len(word) == 0:
      return 0
   else: 
      return 1 + count_letters(word[1:])