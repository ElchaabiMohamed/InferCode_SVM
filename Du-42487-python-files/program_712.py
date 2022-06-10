def reverse_list(l):
   if l == []:
      return []
   return l[1:].append(l[0])