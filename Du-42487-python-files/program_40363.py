def reverse_list (l):
  new = []
  i = 0
  while i < len(l):
    new.append(l[len(l) - i - 1])
  i += 1
	
  return new