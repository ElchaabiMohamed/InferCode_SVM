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
   
   if letter in str:
      return True 
   else:
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
   while i < len(list):
      if list(str) > 1: 
         nums = list[i] + list[i-1]
      else: 
         nums = list[1] - 1 
      list.append(nums)
      i - 1 - i 
   return list[-1]   	
