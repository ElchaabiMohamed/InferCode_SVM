def reverse_list(l):
   if l == []:
      return []
   new = reverse_list(l[1:]).append(l[0])
   return new