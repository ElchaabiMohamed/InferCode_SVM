import time 

def countdown(num):
   i = 0 
   while num != 0: 
      time.sleep(0.1)
      print(num)
      num = num - 1
      i = i + 1   
   print("LIFT OFF!")

def search(str,letter):
   i = 0
   while i < len(str):
      if str[i] == letter:
         return True 
      i = i + 1 
   return False        


def index(str, letter):
	i = 0 
	while i < len(str):
	   if str[i] == letter:
	      return i 
	   else:
	       i = i + 1 
	if i == len(str):
	   return "-1"        

def fibonacci(n):
   list = [0]
   i = 0 
   while n >= len(list):
      if len(list) > 1: 
         new_num = list[i] + list[i-1]
      else: 
         new_num = list[i] + 1 
      list.append(new_num)
      i = i + 1  
   return list[-1]   	
