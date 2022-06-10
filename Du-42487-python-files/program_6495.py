import time
def countdown(num):
   while num > 0:
      print(num)
      time.sleep(0.1)
      num = num - 1
      if num == 0:
         print("LIFT OFF!")

def search(str,letter):
   if letter in str:
      return True
   else:
      return False

def index(str,letter):
   if letter in str:
      return(str[letter])
   else:
      return -1
