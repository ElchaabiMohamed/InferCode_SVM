def reverse_list(list):
   if not list:
      return list
   else:
      return(list[-1] + reverse_list(list))