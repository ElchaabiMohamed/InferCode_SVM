def search(str,letter):
   if str == []:
      return False
   elif str[0] == letter:
      return True 
   else: 
      return search(str[1:],letter)      
   