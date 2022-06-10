def countdown(num):
   if num == 0:
      print("LIFT OFF!")
   else:
      print(num)
      countdown(num - 1)
      
