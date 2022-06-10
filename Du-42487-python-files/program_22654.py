import time

def countdown(num):
   while num >= 1:
      print(num)
      time.sleep(0.1)
      num = num - 1

   print("LIFT OFF!")

def search(str,letter):
   if letter in str:
      print("True")
   else:
      print("False")

