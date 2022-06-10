def reverse_list(n=[]):
   if len(n)==1:
    return 0
   else:
    return reverse_list(n-1)
