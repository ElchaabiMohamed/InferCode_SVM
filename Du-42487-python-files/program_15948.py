def reverse_list(l):
   if l == []:
      return []
   return reverse_list(l[1:]) + [l[0]]