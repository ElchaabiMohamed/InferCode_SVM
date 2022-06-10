def count_letters(string):
   if not string:
      return 0
   else:
      return(1+count_letters(string.replace(string[0], "")))