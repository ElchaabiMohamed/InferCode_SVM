import time 

def countdown(num):
 i = 0
 while i < num:
  print(num - i)
  time.sleep(0.1)
  i = i + 1
 print("LIFT OFF!")

def search(str,letter):
 if letter in str:
  return "True"
 else:
  return "False" 

def index(str,letter,num):
 n = 0
 if letter in str:
  i = 0
  while i < len(str):
   if letter == str[i]:
    return i
   i = i + 1
 else:
  return "-1"

def fibonacci(n):
 list = [0]
 i = 0
 while n >= len(list):
  if len(list) > 1:
   n2 = list[i] + list[i-1]
  else:
   n2 = list[i] + 1
  list.append(n2)
  i = i + 1
 return list[-1]