def count_letters(m):
   if m == '':
      return 0
   else:
      return 1 + count_letters(m[1:])
