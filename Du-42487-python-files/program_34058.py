def count_letters(n):
  if n == '':
    return 0
  else:
    return count_letters(n[1:]) + 1
