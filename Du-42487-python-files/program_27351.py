def count_letters(s, i=0):
   if i < len(s):
      i = i + 1
      return count_letters(s, i)
   else:
      return i
