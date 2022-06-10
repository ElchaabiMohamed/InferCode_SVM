import time
def countdown(num):
   if num == 1:
      print(num)
      countdown(num-1)
   else:
      print("LIFT OFF!")

    

   
if __name__ == "__main__":
   print("calling countdown(\"num\")")
   print(countdown("num"))