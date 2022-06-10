#


#def search(str,letter):
#   if letter in str:
#      return "True"
#   else:
#      return "False"
 


def search(str, letter):
   i = 0
   while i < len(str):
   	if str[i] == letter:
   		return "True"
   	i = i + 1 
   return "False" 




def fibonacci(n):
   a, b = 0, 1 
   for i in range(n):
      a, b = b,  a + b
   return a 
      

#def fibonacci(n):
   #if n == 0:
    #  return 0
   #if n == 1:
    #  return 1 
   #else:
    #  return fibonacci(n-1) + fibonacci(n-2)