import time
def countdown(num):
   if num == 1:
      print(num)
   else:
      countdown(num-1)

    

   
if __name__ == "__main__":
   print("calling countdown(\"num\")")
   print(countdown("num"))