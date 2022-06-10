def reverse(test):
  b = []
  i = 0
  while i < len(test):
    b.append(test[len(test)-1-i])
    i = i + 1
  return b


