def count_letters(n):
   if len(n)==1:
     return n[0]
   return 1+count_letters(n[0:])
