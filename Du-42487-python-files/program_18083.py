def reverse_list(l):
   return reverse_list(l[1:]) + [l[0]] if l else []