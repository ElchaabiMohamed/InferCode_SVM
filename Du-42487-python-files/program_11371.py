
def count(string):
   if not string:
      return 0
   else:
      return(1+count(string.replace(string[0], "")))