def reverse_list(l):
  if l == []:
    return []
  tmp = reverse_list(l[1:])
  tmp.append(l[0])
  return tmp