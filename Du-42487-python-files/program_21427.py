import time
def countdown(num):
   i = 1
   while i < 101:
      time.sleep(0.1)
      print(101 - i) 
      i = i + 1

   print("LIFT OFF!")
      

   
if __name__ == "__main__":
   print("calling countdown(\"num\")")
   print(countdown("num"))