import time

def countdown(num):
   while int(num) > 0:
      print(num)
      num = num - 1
      time.sleep(0.1)
      
   print("LIFT OFF!")


def search(str,letter):
   if letter in str:
      print("True")
   else:
      print("False")
