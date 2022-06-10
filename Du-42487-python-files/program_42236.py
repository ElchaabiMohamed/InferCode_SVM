#

#def countdown(num):
 #  while num > 0:
  #    print num
   #   num = num - 1
    #  if num == 0:
     #    time.sleep(1.0)
      #   print "LIFT OFF!"
import time 
def countdown(num):
	while num >= 1:
	   print (num)
	   num = num - 1 
	if num == 0:
		time.sleep(1.0)
		print("LIFT OFF!")




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


#def index(str,letter):
 #  i = 0
  # while i < len(str):
   #   if str[i] == letter:
    #     return i 
     # i = i + 1
   #return -1

def index(str,letter,pos):
   i = str[0]
   pos = 1 
   while i < len(str):
      if letter in str:
         pos = i + 1
         return pos
      i = i + 1 
   return "-1"
       

      

#def fibonacci(n):
   #if n == 0:
    #  return 0
   #if n == 1:
    #  return 1 
   #else:
    #  return fibonacci(n-1) + fibonacci(n-2)


def fibonacci(n):
   a, b = 0, 1 
   for i in range(n):
      a, b = b,  a + b
   return a 
      
